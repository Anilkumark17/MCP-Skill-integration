"""Call the Fetch MCP server's `fetch` tool over stdio and save the raw exchange.

SpecGate uses this when the session has no `mcp__fetch__fetch` tool. It launches
the same server as `.mcp.json` (`uvx mcp-server-fetch`), so the evidence comes
from the same MCP tool either way.

Usage:
    python mcp_fetch.py URL OUT_JSON [--max-length 8000] [--start-index 0] [--timeout 60]

Writes OUT_JSON with timestamp, server info, tool list, request and response.
Prints one JSON line: {"isError": ..., "chars": ..., "text": "<first 4000 chars>"}.
Exit code: 0 on a tool result (even isError), 2 on a transport failure or timeout.
"""
import argparse, datetime, json, os, subprocess, sys, threading

p = argparse.ArgumentParser()
p.add_argument('url')
p.add_argument('out_json')
p.add_argument('--max-length', type=int, default=8000)
p.add_argument('--start-index', type=int, default=0)
p.add_argument('--timeout', type=float, default=60)
a = p.parse_args()

proc = subprocess.Popen(['uvx', 'mcp-server-fetch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, text=True, encoding='utf-8')
timer = threading.Timer(a.timeout, proc.kill)
timer.start()


def send(msg):
    proc.stdin.write(json.dumps(msg) + '\n')
    proc.stdin.flush()


def recv(want_id):
    while True:
        line = proc.stdout.readline()
        if not line:
            raise RuntimeError('server closed or timed out after %.0f s' % a.timeout)
        msg = json.loads(line)
        if msg.get('id') == want_id:
            return msg


rec = {'timestamp_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')}
try:
    send({'jsonrpc': '2.0', 'id': 1, 'method': 'initialize',
          'params': {'protocolVersion': '2024-11-05', 'capabilities': {},
                     'clientInfo': {'name': 'specgate', 'version': '1.0'}}})
    rec['server'] = recv(1).get('result', {}).get('serverInfo')
    send({'jsonrpc': '2.0', 'method': 'notifications/initialized'})
    send({'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list'})
    rec['tools'] = [t['name'] for t in recv(2).get('result', {}).get('tools', [])]
    rec['request'] = {'jsonrpc': '2.0', 'id': 3, 'method': 'tools/call',
                      'params': {'name': 'fetch', 'arguments': {
                          'url': a.url, 'max_length': a.max_length, 'start_index': a.start_index}}}
    send(rec['request'])
    rec['response'] = recv(3)
    code = 0
except Exception as e:  # transport failure or timeout: a transient error for SpecGate §5
    rec['transport_error'] = str(e)
    code = 2
finally:
    timer.cancel()
    try:
        proc.stdin.close()
    except Exception:
        pass
    proc.kill()

os.makedirs(os.path.dirname(os.path.abspath(a.out_json)), exist_ok=True)
with open(a.out_json, 'w', encoding='utf-8') as f:
    json.dump(rec, f, indent=2, ensure_ascii=False)

result = rec.get('response', {}).get('result', {})
text = ''.join(c.get('text', '') for c in result.get('content', []))
summary = {'isError': result.get('isError', code != 0), 'chars': len(text),
           'text': text[:4000] if code == 0 else rec.get('transport_error')}
sys.stdout.reconfigure(encoding='utf-8')
print(json.dumps(summary, ensure_ascii=False))
sys.exit(code)
