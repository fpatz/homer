PYTHON=c:/Python27/python

.PHONY: buildout

buildout: bin/buildout.exe
	bin/buildout

bin/buildout.exe:
	$(PYTHON) bootstrap.py

