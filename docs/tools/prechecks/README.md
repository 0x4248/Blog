# Prechecks

The prechecks system checks for the required tools, dependencies, files and folders before the build process starts. The prechecks are called by the makefile before the build process starts.

## Checks

- [bash](bash.md)
- [pip](pip.md)
- [python](python.md)
- [dependencies](dependencies.md)
- [folders](folders.md)

## Makefile

Each precheck is called at the top of the `Makefile` before the build process starts and every precheck target starts with `helthchecks-`.

### Example

```makefile
helthchecks-python:
	@$(BASH) $(TOOLS)/prechecks/python.sh
```

## Hacking

To add a new precheck, create a new script in the `tools/prechecks` folder and add a new target to the `Makefile`.

### Example

Im going to make a new check that checks if `git` is installed.

1. Create a new script in `tools/prechecks/git.sh`:

```bash
# Comments and shebang

if ! which git > /dev/null; then
    echo "git is not installed. Please install git before running the Makefile."
    exit 1
fi
```

2. Add a new target to the `Makefile`:

```makefile
helthchecks-git:
    @$(BASH) $(TOOLS)/prechecks/git.sh
```

3. Add the new target to the `prechecks` target:

```makefile
prechecks: <EVERYTHING ELSE> helthchecks-git
```

4. Done! Now the `git` check will run before the build process starts.