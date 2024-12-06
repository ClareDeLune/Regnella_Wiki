###Set-Up
from contextlib import nullcontext

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

def accessSkill(name, address):
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
    print(address)
    if isNull:
        return accessPageNotFound()
    else:
        skill = {"name": data[1], "type": data[2], "usage": data[3], "element": data[4], "overview": data[5], "description": data[6]}
        print(skill)
        db.close()
        if address == 'Edit':
            return render_template('PageHTML/individSkillEdit.html', name=skill["name"], type=skill["type"], usage=skill["usage"], element=skill["element"], overview=skill["overview"], description=skill["description"], address=address)
        else:
            return render_template('PageHTML/individSkillPage.html', name = skill["name"], type = skill["type"], usage = skill["usage"], element = skill["element"], overview = skill["overview"], description = skill["description"], address=address)


def accessEnemy(name, address):
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
        if address == 'Edit':
            return render_template('PageHTML/individEnemyEdit.html', name=enemy["name"], act=enemy["act"], MHP=enemy["MHP"], MMP=enemy["MMP"], ATK=enemy["ATK"], DEF=enemy["DEF"], MAT=enemy["MAT"], MDF=enemy["MDF"], AGI=enemy["AGI"], LUK=enemy["LUK"], overview=enemy["overview"], description=enemy["description"], address=address)
        else:
            return render_template('PageHTML/individEnemyPage.html', name=enemy["name"], act=enemy["act"], MHP=enemy["MHP"], MMP=enemy["MMP"], ATK=enemy["ATK"], DEF=enemy["DEF"], MAT=enemy["MAT"], MDF=enemy["MDF"], AGI=enemy["AGI"], LUK=enemy["LUK"], overview=enemy["overview"], description=enemy["description"], address=address)

def accessClass(name, address):
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
        if address == 'Edit':
            return render_template('PageHTML/individClassEdit.html', name=classD["name"], baseMHP=classD["sMHP"], baseMMP=classD["sMMP"], baseATK=classD["sATK"], baseDEF=classD["sDEF"], baseMAT=classD["sMAT"], baseMDF=classD["sMDF"], baseAGI=classD["sAGI"], baseLUK=classD["sLUK"], maxMHP=classD["fMHP"], maxMMP=classD["fMMP"], maxATK=classD["fATK"], maxDEF=classD["fDEF"], maxMAT=classD["fMAT"], maxMDF=classD["fMDF"], maxAGI=classD["fAGI"], maxLUK=classD["fLUK"], overview=classD["overview"], description=classD["description"], address=address)
        else:
            return render_template('PageHTML/individClassPage.html', name = classD["name"], baseMHP = classD["sMHP"], baseMMP = classD["sMMP"], baseATK = classD["sATK"], baseDEF = classD["sDEF"], baseMAT = classD["sMAT"], baseMDF = classD["sMDF"], baseAGI = classD["sAGI"], baseLUK = classD["sLUK"], maxMHP = classD["fMHP"], maxMMP = classD["fMMP"], maxATK = classD["fATK"], maxDEF = classD["fDEF"], maxMAT = classD["fMAT"], maxMDF = classD["fMDF"], maxAGI = classD["fAGI"], maxLUK = classD["fLUK"], overview = classD["overview"], description = classD["description"], address=address)


def accessMember(name, address):
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
        if address == 'Edit':
            return render_template('PageHTML/individPartyEdit.html', name=member["name"], level=member["startingLevel"], MHP=member["MHP"], MMP=member["MMP"], ATK=member["ATK"], DEF=member["DEF"], MAT=member["MAT"], MDF=member["MDF"], AGI=member["AGI"], LUK=member["LUK"], support1N=member["support1N"], support1L=member["support1L"], support2N=member["support2N"], support2L=member["support2L"], support3N=member["support3N"], support3L=member["support3L"], support4N=member["support4N"], support4L=member["support4L"], support5N=member["support5N"], support5L=member["support5L"], overview=member["overview"], description=member["description"], address=address)
        else:
            return render_template('PageHTML/individPartyPage.html', name = member["name"], level = member["startingLevel"], MHP = member["MHP"], MMP = member["MMP"], ATK = member["ATK"], DEF = member["DEF"], MAT = member["MAT"], MDF = member["MDF"], AGI = member["AGI"], LUK = member["LUK"], support1N = member["support1N"], support1L = member["support1L"], support2N = member["support2N"], support2L = member["support2L"], support3N = member["support3N"], support3L = member["support3L"], support4N = member["support4N"], support4L = member["support4L"], support5N = member["support5N"], support5L = member["support5L"], overview = member["overview"], description = member["description"], address=address)


def accessLocation(name, address):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM locations  WHERE locations.name = ?"
    args = [name]
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
        if address == 'Edit':
            return render_template('PageHTML/individLocationEdit.html', name=location["name"], act=location["act"], connect=location["connect"], overview=location["overview"], description=location["description"], address=address)
        else:
            return render_template('PageHTML/individLocationPage.html', name = location["name"], act = location["act"], connect = location["connect"], overview = location["overview"], description = location["description"], address=address)


def loadList(tableName):
    db = openDatabase()
    dbc = db.cursor()
    data = []
    if tableName == "Characters":
        sql = "SELECT Characters.firstName, Characters.surname FROM Characters WHERE Characters.type = 'Enemy'"
        foeData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            foeData.append('<tr>')
            foeData.append('<td class="bodyRow">')
            foeData.append('<a href="{{ url_for(')
            foeData.append(str(row))
            foeData.append(') }}">')
            foeData.append(str(row))
            foeData.append('</td>')
            foeData.append('</tr>')
        print(foeData)
        print("\n")
        foeTData = ''.join(foeData)
        print(foeTData)

        sql = "SELECT Characters.firstName, Characters.surname FROM Characters WHERE Characters.type = 'Playable'"
        playData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            playData.append('<tr>')
            playData.append('<td class="bodyRow">')
            playData.append('<a href="{{ url_for(')
            playData.append(str(row))
            playData.append(') }}">')
            playData.append(str(row))
            playData.append('</td>')
            playData.append('</tr>')
        print(playData)
        print("\n")
        playTData = ''.join(playData)
        print(playTData)

        sql = "SELECT Characters.firstName, Characters.surname FROM Characters WHERE Characters.type = 'NPC'"
        npcData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            npcData.append('<tr>')
            npcData.append('<td class="bodyRow">')
            npcData.append('<a href="{{ url_for(')
            npcData.append(str(row))
            npcData.append(') }}">')
            npcData.append(str(row))
            npcData.append('</td>')
            npcData.append('</tr>')
        print(npcData)
        print("\n")
        npcTData = ''.join(npcData)
        print(npcTData)
        return render_template('PageHTML/charList.html', playableTable = playTData, enemyTable = foeTData, npcTable = npcTData)

    elif tableName == "Classes":
        sql = "SELECT Classes.name FROM Classes"
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            data.append('<tr>')
            data.append('<td class="bodyRow">')
            data.append('<a href="{{ url_for(')
            data.append(str(row))
            data.append(') }}">')
            data.append(str(row))
            data.append('</td>')
            data.append('</tr>')
        print(data)
        print("\n")
        tableData = ''.join(data)
        print(tableData)
        return render_template('PageHTML/classList.html', tableData = tableData)

    elif tableName == "Enemies":
        sql = "SELECT Enemies.name FROM Enemies"
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            data.append('<tr>')
            data.append('<td class="bodyRow">')
            data.append('<a href="{{ url_for(')
            data.append(str(row))
            data.append(') }}">')
            data.append(str(row))
            data.append('</td>')
            data.append('</tr>')
        print(data)
        print("\n")
        tableData = ''.join(data)
        print(tableData)
        return render_template('PageHTML/enemyList.html', tableData = tableData)

    elif tableName == "Equipment":
        sql = "SELECT Equipment.name FROM Equipment WHERE Equipment.type = 'Weapon'"
        weaponData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            weaponData.append('<tr>')
            weaponData.append('<td class="bodyRow">')
            weaponData.append('<a href="{{ url_for(')
            weaponData.append(str(row))
            weaponData.append(') }}">')
            weaponData.append(str(row))
            weaponData.append('</td>')
            weaponData.append('</tr>')
        print(data)
        print("\n")
        weaponTData = ''.join(weaponData)
        print(weaponTData)

        sql = "SELECT Equipment.name FROM Equipment WHERE Equipment.type = 'Armour'"
        armourData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            armourData.append('<tr>')
            armourData.append('<td class="bodyRow">')
            armourData.append('<a href="{{ url_for(')
            armourData.append(str(row))
            armourData.append(') }}">')
            armourData.append(str(row))
            armourData.append('</td>')
            armourData.append('</tr>')
        print(armourData)
        print("\n")
        armourTData = ''.join(armourData)
        print(armourTData)

        sql = "SELECT Equipment.name FROM Equipment WHERE Equipment.type = 'Accessory'"
        accData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            accData.append('<tr>')
            accData.append('<td class="bodyRow">')
            accData.append('<a href="{{ url_for(')
            accData.append(str(row))
            accData.append(') }}">')
            accData.append(str(row))
            accData.append('</td>')
            accData.append('</tr>')
        print(accData)
        print("\n")
        accTData = ''.join(accData)
        print(accTData)

        sql = "SELECT Equipment.name FROM Equipment WHERE Equipment.type = 'Spirit'"
        spiritData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            spiritData.append('<tr>')
            spiritData.append('<td class="bodyRow">')
            spiritData.append('<a href="{{ url_for(')
            spiritData.append(str(row))
            spiritData.append(') }}">')
            spiritData.append(str(row))
            spiritData.append('</td>')
            spiritData.append('</tr>')
        print(spiritData)
        print("\n")
        spiritTData = ''.join(spiritData)
        print(spiritTData)
        return render_template('PageHTML/equipList.html', weaponTable = weaponTData, armourTable = armourTData, accTable = accTData, spiritTable = spiritTData)

    elif tableName == "Locations":
        sql = "SELECT Locations.name FROM Location for Location.act = 1"
        actIData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            actIData.append('<tr>')
            actIData.append('<td class="bodyRow">')
            actIData.append('<a href="{{ url_for(')
            actIData.append(str(row))
            actIData.append(') }}">')
            actIData.append(str(row))
            actIData.append('</td>')
            actIData.append('</tr>')
        print(actIData)
        print("\n")
        actITData = ''.join(actIData)
        print(actITData)

        sql = "SELECT Locations.name FROM Location for Location.act = 2"
        actIIData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            actIIData.append('<tr>')
            actIIData.append('<td class="bodyRow">')
            actIIData.append('<a href="{{ url_for(')
            actIIData.append(str(row))
            actIIData.append(') }}">')
            actIIData.append(str(row))
            actIIData.append('</td>')
            actIIData.append('</tr>')
        print(actIIData)
        print("\n")
        actIITData = ''.join(actIIData)
        print(actIITData)

        sql = "SELECT Locations.name FROM Location for Location.act = 3"
        actIIIData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            actIIIData.append('<tr>')
            actIIIData.append('<td class="bodyRow">')
            actIIIData.append('<a href="{{ url_for(')
            actIIIData.append(str(row))
            actIIIData.append(') }}">')
            actIIIData.append(str(row))
            actIIIData.append('</td>')
            actIIIData.append('</tr>')
        print(actIIIData)
        print("\n")
        actIIITData = ''.join(actIIIData)
        print(actIIITData)
        return render_template('PageHTML/locationList.html', act1Table = actIData, act2Table = actIIData, act3Table = actIIIData)


    elif tableName == "PartyMembers":
        sql = "SELECT PartyMembers.firstName, PartyMembers.surname FROM PartyMembers"
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            data.append('<tr>')
            data.append('<td class="bodyRow">')
            data.append('<a href="{{ url_for(')
            data.append(str(row))
            data.append(') }}">')
            data.append(str(row))
            data.append('</td>')
            data.append('</tr>')
        print(data)
        print("\n")
        tableData = ''.join(data)
        print(tableData)
        return render_template('PageHTML/partyList.html', tableData=tableData)


    elif tableName == "Skills":
        sql = "SELECT Skills.name FROM Skills"
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            data.append('<tr>')
            data.append('<td class="bodyRow">')
            data.append('<a href="{{ url_for(')
            data.append(str(row))
            data.append(') }}">')
            data.append(str(row))
            data.append('</td>')
            data.append('</tr>')
        print(data)
        print("\n")
        tableData = ''.join(data)
        print(tableData)
        db.close()
        return render_template('PageHTML/skillList.html', tableData=tableData)
    return accessPageNotFound()


def submitPage():
    return render_template('TemplateHTML/Homepage.html')




def accessPageNotFound():
    print("Page not found!\nSome sort of error page should appear here.")
    return render_template('TemplateHTML/Homepage.html')
