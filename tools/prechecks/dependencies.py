# MarkdownBlog
# Write blogs in markdown and generate static html files that are
# ready to be served by a web server and are hackable.
# Github: https://www.github.com/0x4248/MarkdownBlog
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# Prechecks/dependencies.py
# This script checks if the dependencies are installed

import importlib
import os

deps = ['markdown', 'flask']
had_error = False
pip = 'pip3'

for dep in deps:
    try:
        importlib.import_module(dep)
    except ImportError:
        print(f"Error: {dep} is not installed")
        had_error = True

if had_error:
    print("Failed to check dependencies do you want to install them? (y/n)")
    if input() == 'y':
        os.system(f"{pip} install {' '.join(deps)}")
    else:
        exit(1)