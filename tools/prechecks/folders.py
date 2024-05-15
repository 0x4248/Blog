# MarkdownBlog
# Write blogs in markdown and generate static html files that are
# ready to be served by a web server and are hackable.
# Github: https://www.github.com/0x4248/MarkdownBlog
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# Prechecks/folders.py
# This script checks if the folders in tools/prechecks/conf/folders.conf exist
# If they dont exist, it will report an error and stop the makefile

from lib.conf import get_config
from lib.conf import strip_blank_lines
import os

def check_folders():
    """Check if the folders in the config file exist

    This function reads the config file and checks if the folders exist. 
    If they dont exist, it will report an error and stop the makefile

    Returns:
        bool: True if all the folders exist, False otherwise
    """
    config = get_config('tools/prechecks/conf/folders.conf')

    # This cleans up the config data before checking so we dont treat 
    # blank lines as folders that should exist.
    config = strip_blank_lines(config)
    all_exist = True
    for folder in config:
        if not os.path.exists(folder):
            print(f"Error [Prechecks/folders.py]: {folder} does not exist")
            all_exist = False
    return all_exist

if __name__ == '__main__':
    folder_check_result = check_folders()
    if not folder_check_result:
        print("Error: Some of the folders do not exist and are required for the makefile to run")
        exit(1)
    else:
        exit(0)