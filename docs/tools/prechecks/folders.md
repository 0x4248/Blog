# Folder precheck

The folder precheck is a check that is called by the makefile. It is called in the `helthchecks-folder` target. The script is located in `tools/prechecks/folder.py`.

## How it works

The script reads the `tools/prechecks/conf/folders.conf` file and checks if the folders listed in the file exist. If the folders do not exist, the script will throw an error and stop the build process.

## Hacking

The script is located in `tools/prechecks/folder.py` and the configuration file is located in `tools/prechecks/conf/folders.conf`.

### Hacking config

The config file is just like a gitignore file but instead of ignoring files, it lists the folders that should exist. The folders are listed one per line.

```bash
# This is a comment
folder1
folder2
folder3
```

### Usage

```bash
make helthchecks-folder
```