# MarkdownBlog
# Write blogs in markdown and generate static html files that are
# ready to be served by a web server and are hackable.
# Github: https://www.github.com/0x4248/MarkdownBlog
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# src/lib/logger.py
# Main logging functions.

from lib import colour

def log(str):
    print("[  " + colour.BLUE + "LOG" + colour.RESET + "  ] " + str)

def warning(str):
    print("[ " + colour.YELLOW + "WARN" + colour.RESET + " ] " + str)

def error(str):
    print("[ " + colour.RED + "ERR" + colour.RESET + "  ] " + str)

def success(str):
    print("[  " + colour.GREEN + "OK" + colour.RESET + "   ] " + str)

def debug(str):
    print("[  " + colour.CYAN + "DBG" + colour.RESET + "  ] " + str)