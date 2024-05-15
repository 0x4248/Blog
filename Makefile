# MarkdownBlog
# Write blogs in markdown and generate static html files that are
# ready to be served by a web server and are hackable.
# Github: https://www.github.com/0x4248/MarkdownBlog
# Licence: GNU General Public License v3.0
# By: 0x4248
#
# Makefile
# This is used to run the rendering scripts, tools and tests.
# It is also used to install the dependencies and to clean the
# repository from the generated files.

#### Variables ####
# This section defines the variables that are used in the Makefile to
# make it easier to change the values of the variables.

## Python ##
PYTHON = python3
PIP = pip3

## Shell ##
SHELL = /bin/bash
BASH = bash

## Directories ##
# The source directory where the scripts are located.
# A quick brief of the directory structure:
# - src: The source directory for the scripts and rendering tools.
# - content: The directory where the markdown files, images, css and js
#   files are located.
# - www: The directory where the generated html files are located.
# - tools: The directory where the tools are located.
SRC = src
CONTENT = content
TOOLS = tools
WWW = www

## Files ##
MAIN = $(SRC)/main.py

## PHONY ##
# This section defines the phony targets that are used in the Makefile.
# Phony targets are the targets that are not files and are used to run
# commands.

PHONY = all

#### All ####
all: prechecks init main

#### Prechecks ####
# This section checks is like a health check to make sure that the
# dependencies are installed and the directories are present.

## Bash ##
# Check if bash is installed by checking the path of the bash executable.
$(if $(shell which $(BASH)),,$(error $(BASH) is not installed. Please install $(BASH) before running the Makefile.))

## Tools directory ##
# Check if the tools directory is present.
$(if $(wildcard $(TOOLS)),,$(error The tools directory is missing please reclone the repository.))

## Python ##
# Check if python is installed by runing tools/prechecks/python.sh
helthchecks-python:
	@$(BASH) $(TOOLS)/prechecks/python.sh

## Pip ##
# Check if pip is installed by runing tools/prechecks/pip.sh
helthchecks-pip:
	@$(BASH) $(TOOLS)/prechecks/pip.sh

## Dependencies ##
# Check if the dependencies are installed by running 
# tools/prechecks/dependencies.py

helthchecks-dependencies:
	@$(PYTHON) $(TOOLS)/prechecks/dependencies.py

## Folder structure ##
# Check if all the folders listed in tools/prechecks/conf/folders.conf
# are present.
helthchecks-folders:
	@$(PYTHON) $(TOOLS)/prechecks/folders.py

## All prechecks ##
# Runs all the prechecks and gets called by the all target.
prechecks: helthchecks-python helthchecks-pip helthchecks-dependencies helthchecks-folders

## PHONY ##
PHONY += prechecks helthchecks-python helthchecks-pip helthchecks-dependencies helthchecks-folders


#### Init ####
# This section is used to initialize the repository by creating the
# directories that are needed to run the scripts.
init: 
	@mkdir -p $(WWW)

## PHONY ##
PHONY += init

#### Clean ####
# These targets are used to clean the repository from the generated files.
clean:
	@rm -rf $(WWW)

rebuild: clean all

## PHONY ##
PHONY += clean rebuild

#### CSS ####
# These targets are used to create the custom.css file
# and to restore the base.css file.

css-create-custom:
	@mv $(CONTENT)/css/base.css $(CONTENT)/css/custom.css

css-restore-base: css-create-custom

## PHONY ##
PHONY += css-create-custom css-restore-base

#### Main ####
# This section defines the main target that is used to run the main.py script

main:
	@$(PYTHON) $(MAIN)

## PHONY ##
PHONY += main 

#### Help ####

help:
	@echo "MarkdownBlog Makefile"
	@echo "This Makefile is used to run the rendering scripts, tools and tests."
	@echo "It is also used to install the dependencies and to clean the repository from the generated files."
	@echo ""
	@echo "Usage:"
	@echo "  make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  all: Run all the targets."
	@echo "  prechecks: Run the prechecks."
	@echo "  init: Initialize the repository."
	@echo "  clean: Clean the repository from the generated files."
	@echo "  rebuild: Clean the repository and run all the targets."
	@echo "  css-create-custom: Create the custom.css file."
	@echo "  css-restore-base: Restore the base.css file."
	@echo "  main: Run the main.py script."
	@echo "  help: Show this help message."
	@echo ""
	@echo "Phony targets:"
	@echo "  $(PHONY)"

## PHONY ##
PHONY += help

#### PHONY ####

.PHONY: $(PHONY)