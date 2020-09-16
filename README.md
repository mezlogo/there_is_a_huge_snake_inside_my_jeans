###This is the first steps snake project.

Example shows how to build and develop artifact using standard python ecosystem:
- `pip`: for dependencies management
- `venv`: for project isolation. By default python installs user or system wide dependencies
- `dependencies.txt` contains pip dependencies and version for reproducible builds
- `src` contains source code

Getting started:
1) install venv for python project isolation: `python -m venv .`
1.alt) For Windows: To use BASH you can install Cygwin, for instance.
2) **BASH ONLY** activate venv for shell: `source bin/activate`
2.alt) For Windows: You need to change directory to /Scripts and perform next commands: first - `set -o igncr`, second - `source activate
` 
3) install manual declared dependencies: `pip install -r dependencies.txt`
4) you can list installed dependencies: `ls -al lib/python3.8/site-packages`
4.alt) For Windows: `ls -al lib/site-packages`
5) run script: `python src/hello.py`
6) download chrome driver: `https://sites.google.com/a/chromium.org/chromedriver/`
7) modify path to chrome in `src/globals.py`
8) create and manipulate chrome using: `python src/open.py`
9) open chrome with remote address: `chromium --remote-debugging-port=9222 --user-data-dir=/tmp/chrometmp`
10) connect to created browser: `python src/remote.py`