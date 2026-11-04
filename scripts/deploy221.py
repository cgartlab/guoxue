# -*- coding: utf-8 -*-
"""通过 gh API 部署第221课到 cgartlab/guoxue main 分支。"""
import base64, io, json, subprocess, sys, difflib

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
print('remote head:', head_sha)

files = [
    'lessons/221-sui-han-song-bai/index.html',
    'assets/js/lessons-manifest.js',
    'sitemap.xml',
    'index.html',
    'tests/homepage.spec.js',
]

tree_items = []
for f in files:
    local = io.open(f, encoding='utf-8', newline='').read()
    try:
        r = json.loads(gh(['repos/%s/contents/%s?ref=%s' % (REPO, f, head_sha)], allow_404=True))
        if r is None:
            raise Exception('not found')
        remote = base64.b64decode(r['content']).decode('utf-8')
        if remote == local:
            print('SAME  %s（跳过）' % f); continue
        diff = list(difflib.unified_diff(remote.splitlines(), local.splitlines(), lineterm=''))
        adds = sum(1 for l in diff if l.startswith('+') and not l.startswith('+++'))
        dels = sum(1 for l in diff if l.startswith('-') and not l.startswith('---'))
        print('DIFF %s: +%d -%d' % (f, adds, dels))
        for l in diff[2:12]:
            print('   ', l[:150])
    except SystemExit:
        raise
    except Exception:
        print('NEW   %s（远程不存在）' % f)
    b = json.loads(gh(['repos/%s/git/blobs' % REPO], method='POST',
                      inp=json.dumps({'content': base64.b64encode(local.encode('utf-8')).decode(),
                                      'encoding': 'base64'})))
    tree_items.append({'path': f, 'mode': '100644', 'type': 'blob', 'sha': b['sha']})
    print('blob  %s -> %s' % (f, b['sha'][:10]))

if not tree_items:
    print('没有需要部署的文件'); sys.exit(0)

tree = json.loads(gh(['repos/%s/git/trees' % REPO], method='POST',
                     inp=json.dumps({'base_tree': base_tree, 'tree': tree_items})))
print('new tree:', tree['sha'][:10])
msg = ('feat(lesson220): 新增《岁寒松柏 · 冷了才看得出》课件（子罕第二十八章）；'
       '首页课程数 221、manifest/sitemap/测试同步')
new_commit = json.loads(gh(['repos/%s/git/commits' % REPO], method='POST',
                           inp=json.dumps({'message': msg, 'tree': tree['sha'], 'parents': [head_sha]})))
print('new commit:', new_commit['sha'][:10])
upd = json.loads(gh(['repos/%s/git/refs/heads/main' % REPO], method='PATCH',
                    inp=json.dumps({'sha': new_commit['sha'], 'force': False})))
print('ref updated:', upd['object']['sha'][:10])
print('DEPLOY OK')
