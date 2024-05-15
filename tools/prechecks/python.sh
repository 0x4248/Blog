# MarkdownBlog
# Write blogs in markdown and generate static html files that are
# ready to be served by a web server and are hackable.
# Github: https://www.github.com/0x4248/MarkdownBlog
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# Prechecks/python
# Checks if python is installed

PYTHON=python3

if ! command -v $PYTHON &> /dev/null; then
    echo "Python3 is not installed"
    exit 1
fi

