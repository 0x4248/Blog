# Bash precheck

This check is not a script but is called in the makefile before anything else is run.

## Check

```make
$(if $(shell which $(BASH)),,$(error $(BASH) is not installed. Please install $(BASH) before running the Makefile.))
```

This check is used to check if the bash shell is installed on the system. If it is not installed, the makefile will throw an error and stop the build process.

## Usage

This cant be called on its own but is called by the makefile before anything else is run.