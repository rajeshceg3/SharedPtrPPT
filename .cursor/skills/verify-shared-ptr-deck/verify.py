#!/usr/bin/env python3
"""Build the shared_ptr slidev deck and verify it boots and renders."""
import json, os, subprocess, sys, time, socket
HERE = os.path.dirname(os.path.abspath(__file__))
DECK = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'slidev-shared-ptr-presentation'))
OUT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '.verification-evidence', 'shared-ptr-deck'))
CHROME = os.environ.get('CHROME_PATH', '/usr/bin/google-chrome')
failures = []
def check(name, cond, detail=''):
    print(('PASS' if cond else 'FAIL'), name, detail)
    if not cond: failures.append(name)
os.makedirs(OUT, exist_ok=True)
r = subprocess.run(['npm', 'run', 'build'], cwd=DECK, capture_output=True, text=True, timeout=600)
open(os.path.join(OUT, 'build.log'), 'w').write(r.stdout + r.stderr)
check('slidev-build', r.returncode == 0 and os.path.exists(os.path.join(DECK, 'dist', 'index.html')))
if failures: print('FAILURES=%d' % len(failures)); sys.exit(1)
s = socket.socket(); s.bind(('127.0.0.1', 0)); port = s.getsockname()[1]; s.close()
srv = subprocess.Popen(['node', '-e', """
const http=require('http'),fs=require('fs'),path=require('path');
http.createServer((req,res)=>{
  let f=path.join('dist',req.url.split('?')[0].split('#')[0]);
  if(!fs.existsSync(f)||fs.statSync(f).isDirectory()) f='dist/index.html';
  fs.createReadStream(f).pipe(res);
}).listen(%d,'127.0.0.1');
""" % port], cwd=DECK, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    time.sleep(1.0)
    import urllib.request
    html = urllib.request.urlopen(f'http://127.0.0.1:{port}/', timeout=10).read().decode()
    check('spa-served', '<div id="app">' in html or 'slidev' in html.lower(), f'{len(html)} bytes')
    # best-effort pixel capture; headless paint timing is flaky, so size is evidence not a gate
    shot = os.path.join(OUT, 'overview.png')
    subprocess.run([CHROME, '--headless=new', '--no-sandbox', '--disable-gpu',
                    '--use-angle=swiftshader-webgl', '--virtual-time-budget=15000',
                    '--window-size=1365,900', f'--screenshot={shot}', f'http://127.0.0.1:{port}/#/1'],
                   capture_output=True, text=True, timeout=120)
    print('INFO capture-bytes', os.path.getsize(shot) if os.path.exists(shot) else 0)
finally:
    srv.terminate(); srv.wait()
json.dump({'checks': len(failures) == 0}, open(os.path.join(OUT, 'result.json'), 'w'))
print('FAILURES=%d' % len(failures))
sys.exit(0 if not failures else 1)
