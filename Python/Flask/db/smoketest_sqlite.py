"""
An sqlite "smoke test", i.e., a
simple test to see if it seems to be
working.  This is *not* the sort of test
suite we would use for regression testing.
It's just a sort of "is this on? is it
working at all?" simple test.
"""
import db_sqlite as db

db.write_rant("Get off my lawn")
db.write_rant("I no longer like turtles")
contents = db.read_rants()
print(contents)

