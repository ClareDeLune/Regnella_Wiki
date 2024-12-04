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
    sql = "SELECT * FROM characters WHERE characters.FirstName = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
            data.append(str(row))
    print(data)
    character = {"firstName": data[1], "lastName": data[2], "age": data[3], "race": data[4], "family": data[5], "type": data[6], "location": data[6], "overview": data[7], "description": data[8]}
    return render_template('PageHTML/individCharPage.html', firstName = character["firstName"], lastName = character["lastName"], age = character["age"], race = character["race"], family = character["family"], type = character["type"], location = character["location"], overview = character["overview"], description = character["description"],)



