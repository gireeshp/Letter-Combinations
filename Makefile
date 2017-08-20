.PHONY: clean install all

clean:
	@echo 'cleaning all cache files'
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

install:
	@echo 'installing...'
	pip install -r requirements.txt

all: clean install
