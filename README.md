# Python Executable

This is a trivial excercise to pack a python script with its dependencies
into an executable zip file.

## Project structure

The `app/` folder contains the source files of the app (`main.py`, etc).

The `packages/` folder contains the dependencies installed via `pip` based
on `requirements.txt`.

## Install dependencies

    make deps

This command installs the dependecies listed in `requirements.txt` into
the `packages/` folder.

## Local test run

    make run

This command executes `app/main.py` as a simple smoke test that the
dependencies in the `packages/` folder are correct.

### Pack

    make

This command combines `app/` and `packages/` and creates a zip file.
It also add `__main__.py` to the root of the archive. This fill imports
`main.py` from the `app/` folder, that is why the `main.py` must exists
because this is the entry point of the executable.

This command produces two files eventually.

The first file is `exe.zip`, which is the standard zip archive.
This file can be run by `python exe.zip` command.

The second file is `exe.pyz`. This file is executable and contains
the "shebang" prefix to `/bin/usr/python3`. Literally, this file is the
contatenation of the "shebang" `#!/bin/usr/python3` line and the `exe.zip`.

This file can be execute just by as `exe.pyz`. Obviously, the python 3
interpreter must be avaiable on the target system at `/usr/bin/python3`.
