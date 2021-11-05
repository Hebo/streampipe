.PHONY: test build
.DEFAULT: build


build:
	echo "nothing to do"

test:
	poetry run pytest
