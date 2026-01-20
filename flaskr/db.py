# Glory be to the LORD our GOD

# Import libraries
import sqlite3
from datetime import datetime
import click
from flask import current_app, g


# create the database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        return g.db
    
def close_Db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()