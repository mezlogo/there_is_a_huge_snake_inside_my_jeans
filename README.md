###This is the first steps snake project.

Example shows how to build and develop artifact using standard python ecosystem:
- `pip`: for dependencies management
- `venv`: for project isolation. By default python installs user or system wide dependencies
- `dependencies.txt` contains pip dependencies and version for reproducible builds
- `src` contains source code

Getting started:
1. Install venv for python project isolation: `python -m venv .`

**For Windows**: To use BASH you can install Cygwin, for instance
  
2. **BASH ONLY** activate venv for shell: `source bin/activate`

**For Windows**: You need to change directory to /Scripts and perform next commands: first - `set -o igncr`, second - `source activate
` 

3. Install manual declared dependencies: `pip install -r dependencies.txt`

4. You can lis. Fort installed dependencies: `ls -al lib/python3.8/site-packages`

**For Windows**: `ls -al lib/site-packages`
  
5. Run script: `python src/hello.py`
6. Download chrome driver: `https://sites.google.com/a/chromium.org/chromedriver/`
7. Modify path to chrome in `src/globals.py`
8. Create and manipulate chrome using: `python src/open.py`
9. Open chrome with remote address: `chromium --remote-debugging-port=9222 --user-data-dir=/tmp/chrometmp`
10. Connect to created browser: `python src/remote.py`