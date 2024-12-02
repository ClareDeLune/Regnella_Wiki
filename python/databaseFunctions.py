###Set-Up
from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)


def openDatabase():
    def create_database():
        db_location = 'database/regnellaDB.db'

        database = getattr(g, 'database', None)
        if database is None:
            database = sqlite3.connect(db_location)
            g.database = database
        return database

def closeDatabase(exception):
    database = getattr(g, 'database' , None )
    if database is not None:
        database.close()


def accessChar(id):
    db = openDatabase()
    try:
        dbc = db.cursor()

        data = []
        sql = "SELECT * FROM characters WHERE characters.FirstName = (%id)", id
        for column in db.cursor().execute(sql):
            data.append(str(column))

        character = {"firstName": data[0], "lastName": data[1], "age": data[2], "race": data[3], "family": data[4], "type": data[5], "location": data[6]}
        return render_template('PageHTML/individCharPage.html', character=character)
    except:
        print("An error has occured while trying to access the database.<br>Please try again later.")
        return render_template('PageHTML/individCharPage.html')




