import os
from pathlib import Path
from shutil import copytree, ignore_patterns, make_archive, rmtree
from distutils.dir_util import copy_tree

EXE = 'exe'
cwd = Path(os.getcwd())

dist = cwd / 'dist'
dist.exists() and dist.is_dir() and rmtree(dist)

dist_clean = cwd / 'dist_clean'
dist_clean.exists() and dist_clean.is_dir() and rmtree(dist_clean)

app = cwd / 'app'
packages = cwd / 'packages'

runner = "import main"

ignores = ignore_patterns(
    '*.pyc',
    'tmp*',
    '__pycache__',
    '*egg-info',
    '*dist-info',
    'bin',
)

print(f"- copying {app} to {dist}")
copytree(app, dist)

print(f"- copying {packages} to {dist}")
copy_tree(str(packages), str(dist))

print(f"- creating ./__main__.py in {dist}")
open(dist / '__main__.py', 'w').write(runner)

print(f"- copying {dist} to {dist_clean}")
copytree(dist, dist_clean, ignore=ignores)

print(f'- zipping {dist_clean} to {EXE}.zip')
make_archive(EXE, 'zip', dist_clean)

print(f'- removing {dist_clean}')
rmtree(dist_clean)

print(f'- removing {dist}')
rmtree(dist)
