# Makefile for database component

###
# You may need to configure these variables:
###
PY = python3      # You might need a specific version like python3.4

install:  sqlite.db
	# just make sure sqlite.db exists

sqlite.db:
	touch sqlite.db
	$(PY)  initdb-sqlite.py

clean:
	rm -f sqlite.db



