###Set-Up
from python.globalFunctions import *

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
    sql = "SELECT * FROM characters  WHERE characters.FirstName = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            data.append(str(item))
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        character = {"name": data[1] + " " + data[2], "firstName": data[1], "lastName": data[2], "age": data[3], "race": data[4], "family": data[5], "type": data[6], "location": data[7], "overview": data[8], "description": data[9]}
        print(character)
        db.close()
        return render_template('PageHTML/individCharPage.html', name = character["name"], firstName = character["firstName"], lastName = character["lastName"], age = character["age"], race = character["race"], family = character["family"], type = character["type"], location = character["location"], overview = character["overview"], description = character["description"])

def accessSkill(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM skills  WHERE skills.name = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            data.append(str(item))
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        skill = {"name": data[1], "type": data[2], "usage": data[3], "element": data[4], "overview": data[5], "description": data[6]}
        print(skill)
        db.close()
        return render_template('PageHTML/individSkillPage.html', name = skill["name"], type = skill["type"], usage = skill["usage"], element = skill["element"], overview = skill["overview"], description = skill["description"])

#Add Functionality
def accessEnemy(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM skills  WHERE skills.name = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            data.append(str(item))
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        skill = {"name": data[1], "type": data[2], "usage": data[3], "element": data[4], "overview": data[5], "description": data[6]}
        print(skill)
        db.close()
        return render_template('PageHTML/individSkillPage.html', name = skill["name"], type = skill["type"], usage = skill["usage"], element = skill["element"], overview = skill["overview"], description = skill["description"])

#Add Functionality
def accessClass(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM skills  WHERE skills.name = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            data.append(str(item))
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        skill = {"name": data[1], "type": data[2], "usage": data[3], "element": data[4], "overview": data[5], "description": data[6]}
        print(skill)
        db.close()
        return render_template('PageHTML/individSkillPage.html', name = skill["name"], type = skill["type"], usage = skill["usage"], element = skill["element"], overview = skill["overview"], description = skill["description"])

#Add Functionality
def accessMember(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM skills  WHERE skills.name = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            data.append(str(item))
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        skill = {"name": data[1], "type": data[2], "usage": data[3], "element": data[4], "overview": data[5], "description": data[6]}
        print(skill)
        db.close()
        return render_template('PageHTML/individSkillPage.html', name = skill["name"], type = skill["type"], usage = skill["usage"], element = skill["element"], overview = skill["overview"], description = skill["description"])

#Add Functionality
def accessLocation(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM skills  WHERE skills.name = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            data.append(str(item))
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        skill = {"name": data[1], "type": data[2], "usage": data[3], "element": data[4], "overview": data[5], "description": data[6]}
        print(skill)
        db.close()
        return render_template('PageHTML/individSkillPage.html', name = skill["name"], type = skill["type"], usage = skill["usage"], element = skill["element"], overview = skill["overview"], description = skill["description"])


def accessPageNotFound():
    print("Page not found!\nSome sort of error page should appear here.")
    return render_template('TemplateHTML/Homepage.html')
