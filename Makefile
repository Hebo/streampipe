.PHONY: test build build-prod
.DEFAULT: build


build:
	# Alias built script to development folder for quick
	# testing without rebuilding
	poetry run python setup.py py2app -A

build-prod:
	poetry run python setup.py py2app

test:
	poetry run pytest
