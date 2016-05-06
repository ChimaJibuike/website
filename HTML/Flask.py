app = Flask(__name__)
app.debug = True


import sqlite3
from flask import g

DATABASE = './database.db'


def connect_to_database():
    db = sqlite3.connect(DATABASE)
    
    with db:
        db.execute('CREATE TABLE if not exists messages(pkey integer primary key, firstname,lastname,email,country,comment)')
    return db

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close() 

@app.route('/')
@app.route('/Home.html')
def Home():
    return render_template('Home.html')
