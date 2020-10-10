# MinimumWebService

A very simple web application written in Python with the 
Flask package.  (Example for CIS 422 students.)

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
