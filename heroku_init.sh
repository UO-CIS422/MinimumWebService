#! /bin/bash
#
# Initialization under Heroku cloud server.  Similar to
# the 'make install' step on ix-dev.  However, Heroku takes
# care of installing the Python libraries, so we skip those
# steps.
#
# Instead of allowing manual editing of configuration file,
# we'll generate a configuration file with a unique random
# string.  The PORT variable will not be used, but we'll provide
# it in case the program tries to use it.
#
# A 'here' document in a script is copied to standard input with substitutions
cat >CONFIG.py <<EOF
COOKIE_KEY = "$$ is the process number in Unix"
DEBUG = False  # Remote debugging is hard, but we could turn this on
PORT = 5000    # Won't be used on Heroku
EOF

# Similar to how we initialized database in db/Makefile.
# Note this database is only for temporary storage because
# the Heroku filesystem is NOT persistent.
#
(cd db ; python initdb-sqlite.py)

