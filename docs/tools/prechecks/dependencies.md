# Dependencies precheck

This is a check that is called by the makefile. It is called in the `helthchecks-dependencies` target. The script is located in `tools/prechecks/dependencies.py`.

The script checks if the dependencies are installed from an array named `deps`.

## Hacking

To add a new dependency to the precheck, add the name of the dependency to the `deps` array in `tools/prechecks/dependencies.py`.

```python
deps = ['deps1', 'deps2', 'deps3']
```

## Usage

```bash
make helthchecks-dependencies
```