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


def accessEnemy(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM enemies WHERE enemies.name = ?"
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
        enemy = {"name": data[1], "act": data[2], "MHP": data[3], "MMP": data[4], "ATK": data[5], "DEF": data[6], "MAT": data[7], "MDF": data[8], "AGI": data[9], "LUK": data[10], "overview": data[11], "description": data[12]}
        print(enemy)
        db.close()
        return render_template('PageHTML/individEnemyPage.html', name = enemy["name"], act = enemy["act"], MHP = enemy["MHP"], MMP = enemy["MMP"], ATK = enemy["ATK"], DEF = enemy["DEF"], MAT = enemy["MAT"], MDF = enemy["MDF"], AGI = enemy["AGI"], LUK = enemy["LUK"], overview = enemy["overview"], description = enemy["description"])


def accessClass(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM classes  WHERE classes.name = ?"
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
        classD = {"name": data[1], "sMHP": data[2], "sMMP": data[3], "sATK": data[4], "sDEF": data[5], "sMAT": data[6], "sMDF": data[7], "sAGI": data[8], "sLUK": data[9], "fMHP": data[10], "fMMP": data[11], "fATK": data[12], "fDEF": data[13], "fMAT": data[14], "fMDF": data[15], "fAGI": data[16], "fLUK": data[17], "overview": data[18], "description": data[19]}
        print(classD)
        db.close()
        return render_template('PageHTML/individClassPage.html', name = classD["name"], baseMHP = classD["sMHP"], baseMMP = classD["sMMP"], baseATK = classD["sATK"], baseDEF = classD["sDEF"], baseMAT = classD["sMAT"], baseMDF = classD["sMDF"], baseAGI = classD["sAGI"], baseLUK = classD["sLUK"], maxMHP = classD["fMHP"], maxMMP = classD["fMMP"], maxATK = classD["fATK"], maxDEF = classD["fDEF"], maxMAT = classD["fMAT"], maxMDF = classD["fMDF"], maxAGI = classD["fAGI"], maxLUK = classD["fLUK"], overview = classD["overview"], description = classD["description"])


def accessMember(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM PartyMembers  WHERE PartyMembers.firstName = ?"
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
        member = {"name": data[1] + " " + data[2], "startingLevel": data[3], "MHP": data[4], "MMP": data[5], "ATK": data[6], "DEF": data[7], "MAT": data[8], "MDF": data[9], "AGI": data[10], "LUK": data[11], "support1N": data[12], "support1L": data[13], "support2N": data[14], "support2L": data[15], "support3N": data[16], "support3L": data[17], "support4N": data[18], "support4L": data[19], "support5N": data[20], "support5L": data[21], "overview": data[22], "description": data[23]}
        print(member)
        db.close()
        return render_template('PageHTML/individPartyPage.html', name = member["name"], level = member["startingLevel"], MHP = member["MHP"], MMP = member["MMP"], ATK = member["ATK"], DEF = member["DEF"], MAT = member["MAT"], MDF = member["MDF"], AGI = member["AGI"], LUK = member["LUK"], support1N = member["support1N"], support1L = member["support1L"], support2N = member["support2N"], support2L = member["support2L"], support3N = member["support3N"], support3L = member["support3L"], support4N = member["support4N"], support4L = member["support4L"], support5N = member["support5N"], support5L = member["support5L"], overview = member["overview"], description = member["description"])


def accessLocation(name):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM locations  WHERE locations.name = ?"
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
        location = {"name": data[1], "act": data[2], "connect": data[3], "overview": data[4], "description": data[5]}
        print(location)
        db.close()
        return render_template('PageHTML/individLocationPage.html', name = location["name"], act = location["act"], connect = location["connect"], overview = location["overview"], description = location["description"])


def accessPageNotFound():
    print("Page not found!\nSome sort of error page should appear here.")
    return render_template('TemplateHTML/Homepage.html')
