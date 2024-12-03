###Set-Up
from flask import Flask, render_template, g
import sqlite3, os

app = Flask(__name__)


def openDatabase():
    base = os.path.abspath(os.path.dirname(__name__))
    db_location = base + "\database\RegnellaDB.db"
    database = getattr(g, 'database', None)
    if database is None:
        database = sqlite3.connect(db_location)
        g.database = database
    return database

def closeDatabase(exception):
    database = getattr(g, 'database' , None )
    if database is not None:
        database.close()


def accessChar(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM characters WHERE characters.FirstName = (%name)", name
    for column in db.cursor().execute(sql):
            data.append(str(column))

    character = {"firstName": data[0], "lastName": data[1], "age": data[2], "race": data[3], "family": data[4], "type": data[5], "location": data[6]}
    return render_template('PageHTML/individCharPage.html', character=character)



