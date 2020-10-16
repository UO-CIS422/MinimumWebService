# Subdirectory db: What is here?

__init__.py is an empty file that is apparently required for me to
import modules stored in this directory.

initdb-sqlite.py is a script that initializes a database sqlite.db .
The file sqlite.db is not in github;  running initdb-sqlite.py
(typically from the Makefile) is what creates it. 

Note: When using the Heroku cloud hosting service, 
SQLite can be used for temporary storage only. 
SQLite keeps the database in the local file system,
and Heroku wipes out and reinitializes the local file
system periodically.   If you need *permanent* storage
for a Heroku app, you need to use an external 
database or storage system like MongoDB or 
an Amazon S3 container. 


