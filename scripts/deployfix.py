# -*- coding: utf-8 -*-
"""通过 gh API 部署第667课到 cgartlab/guoxue main 分支。"""
import base64, io, json, subprocess, sys

REPO = 'cgartlab/guoxue'

def gh(args, inp=None, allow_404=False, method='GET'):
    cmd = ['gh', 'api', '-X', method] + args
    if inp is not None:
        cmd += ['--input', '-']
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8',
                       input=inp, errors='replace')
    if r.returncode != 0:
        if allow_404 and '404' in r.stderr:
            return None
        print('GH FAIL:', args, r.stderr[:500]); sys.exit(1)
    return r.stdout

ref = json.loads(gh(['repos/%s/git/ref/heads/main' % REPO]))
head_sha = ref['object']['sha']
commit = json.loads(gh(['repos/%s/git/commits/%s' % (REPO, head_sha)]))
base_tree = commit['tree']['sha']
print('remote head:', head_sha, '|', commit['message'].splitlines()[0][:60])

files = [
    'lessons/666-huai-dui-liu/index.html',
    'lessons/667-kai-xue-zhang/index.html',
    'scripts/deployfix.py',
]

tree_items = []
for f in files:
    local = io.open(f, encoding='utf-8', newline='').read()
    b = json.loads(gh(['repos/%s/git/blobs' % REPO], method='POST',
                      inp=json.dumps({'content': base64.b64encode(local.encode('utf-8')).decode(),
                                      'encoding': 'base64'})))
    tree_items.append({'path': f, 'mode': '100644', 'type': 'blob', 'sha': b['sha']})
    print('blob  %s -> %s (%d bytes)' % (f, b['sha'][:10], len(local.encode('utf-8'))))

tree = json.loads(gh(['repos/%s/git/trees' % REPO], method='POST',
                     inp=json.dumps({'base_tree': base_tree, 'tree': tree_items})))
print('new tree:', tree['sha'][:10])
msg = 'fix(mobile): 第666/667课 viewport 元标签缺 width=device-width，手机端整页被缩放至 1/2.6、字号偏小；已改为与第665课一致'
new_commit = json.loads(gh(['repos/%s/git/commits' % REPO], method='POST',
                           inp=json.dumps({'message': msg, 'tree': tree['sha'], 'parents': [head_sha]})))
print('new commit:', new_commit['sha'][:10])
upd = json.loads(gh(['repos/%s/git/refs/heads/main' % REPO], method='PATCH',
                    inp=json.dumps({'sha': new_commit['sha'], 'force': False})))
print('ref updated:', upd['object']['sha'][:10])
print('DEPLOY OK')
