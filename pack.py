import os
import shutil
import site
from pathlib import Path
from shutil import copytree, ignore_patterns, rmtree

DIST = os.getcwd() + '/dist'

dist = Path(DIST)
if dist.exists() and dist.is_dir():
    shutil.rmtree(dist)

PACKAGES = "packages"
packages = dist / PACKAGES

runner = "import app.main"

requirements = map(
    lambda x: x.split('==')[0].replace('-', '_').strip(),
    open('deps.txt').readlines(),
)
requirements = set(requirements)
print('- requirements ', requirements)

ignores = ignore_patterns(
    '*.pyc',
    'tmp*',
    '__pycache__',
    '*egg-info',
    '*dist-info',
)

for folder_ in site.getsitepackages():
    folder = Path(folder_)
    print(f'- adding dependencies from {folder}')

    deps = list(filter(lambda x: x in requirements, os.listdir(folder)))

    for dep in deps:
        copytree(folder / dep, packages / dep, ignore=ignores)

print(f"- copying {os.getcwd()}/app/* to {packages / 'app'}")
copytree(os.getcwd() + '/app', packages / 'app', ignore=ignores)

print(f"- creating ./__main__.py in {packages}")
with open(packages / '__main__.py', 'w') as f:
    f.write(runner)

print(f'- zipping {dist/packages} to {dist/"packages.zip"}')
shutil.make_archive(dist / 'exe', 'zip', dist / packages)

print(f'- removing {dist/packages}')
rmtree(dist / 'packages')
