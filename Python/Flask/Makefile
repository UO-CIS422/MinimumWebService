#
# 'make build' should install needed Python modules and
# initialize CONFIG.py
#
# 'make go' should run the applicaton
#
# 

###
# You may need to configure these variables:
###
PY = python3      # You might need a specific version like python3.4
PYVENV = pyvenv   # You might need a specific version like pyvenv-3.4

install:	CONFIG.py
	rm -rf env  # In case it is already there
	$(PYVENV) env
	(. env/bin/activate ; pip3 install -r requirements.txt)

go:	env CONFIG.py
	(. env/bin/activate; $(PY) flask_main.py)

env:
	build

CONFIG.py:  CONFIG.base.py
	echo "Warning: Copying CONFIG.py from base version; it may need editing"
	cp CONFIG.base.py CONFIG.py

