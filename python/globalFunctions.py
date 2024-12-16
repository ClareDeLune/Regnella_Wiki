###Set-Up for libraries used by all other Python files; did contain non-database functions, but this caused errors so they
###were moved to databaseFunctions.

from flask import Flask, flash, render_template, g, request
import sqlite3, os, datetime
from python.databaseFunctions import *

app = Flask(__name__)