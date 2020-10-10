#
# 'make build' should install needed Python modules and
# initialize CONFIG.py
#
# 'make test' should run the test server (with debugging)
# 'make run PORT=5656'  should run the flask application under gunicorn on port 5656
#
# 

###
# You may need to configure these variables:
###
PY = python3      # You might need a specific version like python3.4
GUPORT = 5656       # When run from Green Unicorn
install:	CONFIG.py
	rm -rf env  # In case it is already there
	$(PY) -mvenv env
	(. env/bin/activate ; pip3 install -r requirements.txt)
	(cd db ; make install)

# Test environment --- this is how we run it in development, maybe from
# within our IDE like PyCharm or maybe for testing on a server like
# ixdev.cs.uoregon.edu.  This is good for debugging but does not have
# security or robustness for production use.
#
test:	env CONFIG.py
	(. env/bin/activate; $(PY) flask_main.py)

# Production environment --- Green Unicorn is a Web Server Gateway Interface
# (WSGI) that manages the Flask object.  It may create multiple copies of the
# Flask object to handle many concurrent http requests.  Running it at
# 0.0.0.0:9999 means that it allows http connections from anywhere on port
# 9999.  For heavy-duty deployment we might go a step further and use an
# Nginx server to proxy requests to Green Unicorn, which then hands them off
# to the Flask object.  Each layer (Nginx, Gunicorn, Flask) handles a different
# part of the job.  Nginx can accept https (encrypted) connections and forward
# them to an unencrypted (http) connection on Green Unicorn.  Green Unicorn
# can keep several Flask objects running and pass the requests on to one that
# isn't too busy.  The Flask object is where the request is actually handled.
#
run:	env CONFIG.py
	(. env/bin/activate; gunicorn -b 0.0.0.0:$(GUPORT) flask_main:app) &

env:
	build

CONFIG.py:  CONFIG.base.py
	echo "Warning: Copying CONFIG.py from base version; it may need editing"
	cp CONFIG.base.py CONFIG.py

clean:
	rm -rf env
	(cd db ; make clean)