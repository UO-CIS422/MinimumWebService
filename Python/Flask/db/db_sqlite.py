"""
The sqlite database module.
This is designed to be one of multiple
database implementations that can be
dynamically chosen when installing the
flask application.  Currently it's the only
choice, and it is likely to require some
revisions when we create another choice.

See design notes at bottom of file.
"""

import arrow
import sqlite3

DBFILE = "db/sqlite.db"  # Relative to main program, not to this module

sqlite3.enable_callback_tracebacks(True)

def write_rant(rant):
    """
    Insert a rant to the database, tagging it with an ISO-formatted
    timestamp.
    """
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()
    nowstring = arrow.now().isoformat()
    argtuple = (nowstring, rant)
    c.execute("INSERT INTO rants VALUES ( ?, ? )", argtuple)
    conn.commit()
    conn.close()

def read_rants():
    """
    Returns a list of all rants in the database.
    (Bad idea, but simple for now.)
    """
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()
    c.execute("SELECT * FROM rants")
    result = c.fetchall()
    #  Warning: 'fetchmany()' may return just one row! 
    conn.close()
    return result





# Design notes:
#
# Note that SQLite Python module does not allow
# sharing connections between threads. Since we may
# well be in a multi-threaded environment (depending on
# how Flask and Gunicorn manage processes), we will make
# a separate connection for each operation.
#
# This is something that might change when we have multiple
# possible database implementations (e.g., Redis and MongoDB
# in addition to SQLite).  I haven't thought through how
# to gracefully accomodate different approaches to threading.
#

