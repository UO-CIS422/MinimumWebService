# MinimumWebService

A very simple web application written in Python with the 
Flask package.  (Example for CIS 422 students.)

## Running on ix-dev or ix.cs.uoregon.edu 

After cloning: 

Edit the `Makefile`; you might need to modify the setting of the `PY` variable if `python3` isn't the way you run Python 3 on your machine (e.g., if you're in Windows).  Then: 

```
make install
```

Now you should have a `CONFIG.py` file.  You might want to change something in it. 

Then: `make test` or `make run`. 

The `test` target will run the Flask module itself, which gives you the development version
of the web server with debugging.   The `run` target will run the Flask object under a more 
robust program, Green Unicorn, which among other things can run multiple copies of the Flask
object in case you have thousands of users.  You probably won't have thousands of users. 

## Running "in the cloud" on Heroku 

Heroku does not run the Makefile.  Instead, it 
looks for two files: 

* runtime.txt : This identifies the "build pack"
that the application requires.  Heroku has a "build pack"
for each version of Python that it currently supports.

* Procfile  : This tells Heroku how to run the 
application.  The example has two parts. 

  * The 'release' process.  Usually I omit this line, 
  but for this example I need to initialize the database. 
  The first line (`release:`) specifies a command
  for this. 
  * The application itself. 
  The first part (`web:`) tells it that
this will run as a web server.  The rest
(`gunicorn flask_main:app  --log-file -`) is
a Unix command for running the application.  In this
case it says to run _Green Unicorn_ (`gunicorn`)
on the `app` object in module `flask_main`, 
which is in `flask_main.py`.   It also redirects
log messages from the application to the standard output
(which is useful when remotely debugging an application
running "in the cloud"). 

Notice that there is a difference in the way 
Green Unicorn is run on Heroku vs ix-dev.  On 
ix-dev we specified `-b 0.0.0.0:$(GUPORT)` to 
connect it to a unique port.  On Heroku the server
will connect to the default http port, which is 80.
Whereas ix-dev is a shared server, Heroku will give
us a unique (virtual) host on which our application
is the only web server.


