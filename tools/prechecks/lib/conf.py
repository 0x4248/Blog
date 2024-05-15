# MarkdownBlog
# Write blogs in markdown and generate static html files that are
# ready to be served by a web server and are hackable.
# Github: https://www.github.com/0x4248/MarkdownBlog
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# Prechecks/lib/conf.py
# Config library for folder prechecks
# This is called by tools/prechecks/folders.py to 
# read the config file

def get_config(config):
    """Get the config from the file

    The config file is just like a gitignore file but instead of ignoring files, it lists the folders that should exist. The folders are listed one per line.

    ```bash
    # This is a comment
    folder1
    folder2
    folder3
    ```

    Args:
        config (string): The path to the config file

    Returns:
        list: The config file as a list
    """
    try:
        f = open(config, 'r')
        data = f.readlines()
        f.close()
    except FileNotFoundError:
        print("Error [Prechecks/lib/conf.py]: Config file not found")
        exit(1)
    except Exception as e:
        print(f"Error [Prechecks/lib/conf.py]: {e}")
        exit(1)

    ret = []
    for line in data:
        if line[0] == '#':
            continue
        ret.append(line.strip())
    return ret

def strip_blank_lines(config_data):
    """"Strip blank lines from the config data

    This is called after reading the config file to remove any blank lines.
    
    Without this the following error would be raised:
    ```
    Error [Prechecks/folders.py]:  does not exist
    Error [Prechecks/folders.py]:  does not exist
    Error [Prechecks/folders.py]:  does not exist
    ```
    This is because the config file has a blank line at the end and throughput 
    the file. This function removes the blank lines and fixes the error.

    Args:
        config_data (list): The config data

    Returns:
        list: The cleaned config data
    """

    return [line for line in config_data if line != '']