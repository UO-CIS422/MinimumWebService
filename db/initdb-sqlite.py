"""
Initialize an SQLite database
in the db directory.
File name is "sqlite.db".

Designed to be invoked from one level up, i.e.,
run 'python3 db/initdb-sqlite.db' from the
main Flask directory.

M Young, April 2016 for CIS 422
"""

DBFILE = "db/sqlite.db"

import arrow  # Date-Time module, better than the built-in datetime

import sqlite3
conn = sqlite3.connect(DBFILE)
c = conn.cursor()
c.execute("CREATE TABLE rants (date text, rant text)")
nowstring = arrow.now().isoformat()
argtuple = (nowstring,  )
c.execute("INSERT INTO rants VALUES ( ?, 'Sample rant')", argtuple)
conn.commit()

c.execute("SELECT * FROM rants")
print(c.fetchone())

c.execute("DELETE FROM rants WHERE date > ''")
c.execute("SELECT * FROM rants")
print("Printing what's left in database")
print(c.fetchmany())

conn.close()

