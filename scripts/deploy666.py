# -*- coding: utf-8 -*-
"""通过 gh API 部署第666课到 cgartlab/guoxue main 分支。"""
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
    'assets/js/lessons-manifest.js',
    'sitemap.xml',
    'index.html',
    'tests/homepage.spec.js',
    'scripts/deploy666.py',
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
msg = ('feat(liwengduiyun): 第666课《笠翁对韵·十灰·槐对柳，虎对骀》（共666课，十灰开篇）；'
       '首页课程数 666、manifest/sitemap/测试同步')
new_commit = json.loads(gh(['repos/%s/git/commits' % REPO], method='POST',
                           inp=json.dumps({'message': msg, 'tree': tree['sha'], 'parents': [head_sha]})))
print('new commit:', new_commit['sha'][:10])
upd = json.loads(gh(['repos/%s/git/refs/heads/main' % REPO], method='PATCH',
                    inp=json.dumps({'sha': new_commit['sha'], 'force': False})))
print('ref updated:', upd['object']['sha'][:10])
print('DEPLOY OK')
