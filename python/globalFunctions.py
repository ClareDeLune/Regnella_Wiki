###Set-Up
from flask import Flask, flash, render_template, g, request
import sqlite3, os, datetime
from python.databaseFunctions import *

app = Flask(__name__)

'''def accessPageNotFound():
    print("Page not found!\nSome sort of error page should appear here.")
    return render_template('TemplateHTML/Homepage.html')
'''