PYTHON = python

.PHONY = help setup test run

FILES = input output

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

setup:
	virtualenv env

	.\env\Scripts\activate
	
	pip install .

	make run

test:
	${PYTHON} -m pytest
	
run:
	${PYTHON} run.py
