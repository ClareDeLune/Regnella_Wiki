###Set-Up: get all libraries and functions from globalFunctions.
from python.globalFunctions import *

##Sets up the application in Flask.
app = Flask(__name__)

##Defines the path and connection between the python application and the SQLite database, using sqlite3 package.
def openDatabase():
    base = os.path.abspath(os.path.dirname(__name__))
    db_location = base + "\database\RegnellaDB.db"
    database = getattr(g, 'database', None)
    if database is None:
        database = sqlite3.connect(db_location)
        g.database = database
    return database

##In case the database needs closed.
def closeDatabase(exception):
    database = getattr(g, 'database' , None )
    if database is not None:
        database.close()


##A function used to retrieve a specific character's details from the database and display them using the IndividChar page template.
def accessChar(name, address):
    #Opens the database and retrieves the cursor, which will be used for querying later.
    db = openDatabase()
    dbc = db.cursor()

    #Defines character by first name, which might later on create conflicts.
    data = []
    sql = "SELECT * FROM characters  WHERE characters.FirstName = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            stringy = str(item)
            stringy = stringFormat(stringy)
            data.append(stringy)
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        character = {"name": data[1], "charName": data[1] + " " + data[2], "firstName": data[1], "lastName": data[2], "age": data[3], "race": data[4], "family": data[5], "type": data[6], "location": data[7], "overview": data[8], "description": data[9], "img": data[10]}
        print(character)
        db.close()
        #Either returns the read-only version or the editing version of individChar, depending on user choice.
        if address == 'Edit':
            return render_template('PageHTML/individCharEdit.html', name=character["name"], firstName = character["firstName"], lastName = character["lastName"], age = character["age"], race = character["race"], family = character["family"], type = character["type"], location = character["location"], overview = character["overview"], description = character["description"], img = character["img"], address=address)
        else:
            return render_template('PageHTML/individCharPage.html', name=character["name"], firstName=character["firstName"], lastName=character["lastName"], age=character["age"], race=character["race"], family=character["family"], type=character["type"], location=character["location"], overview=character["overview"], description=character["description"], img=character["img"], address=address)

##A function used to retrieve a specific skill's details from the database and display them using the IndividSkill page template.
def accessSkill(name, address):
    #All these accessX functions are very similar, but due to database columns, numbers of arguments, and the template at the end,
    #they couldn't all be handled by the same function.
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM skills  WHERE skills.name = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            stringy = str(item)
            stringy = stringFormat(stringy)
            data.append(stringy)
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    print(address)
    if isNull:
        return accessPageNotFound()
    else:
        skill = {"name": data[1], "type": data[2], "usage": data[3], "element": data[4], "overview": data[5], "description": data[6], "img": data[7]}
        print(skill)
        db.close()
        if address == 'Edit':
            return render_template('PageHTML/individSkillEdit.html', name=skill["name"], type=skill["type"], usage=skill["usage"], element=skill["element"], overview=skill["overview"], description=skill["description"], img = skill["img"], address=address)
        else:
            return render_template('PageHTML/individSkillPage.html', name = skill["name"], type = skill["type"], usage = skill["usage"], element = skill["element"], overview = skill["overview"], description = skill["description"], img = skill["img"], address=address)

##A function used to retrieve a specific enemy's details from the database and display them using the IndividEnemy page template.
def accessEnemy(name, address):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM enemies WHERE enemies.name = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            stringy = str(item)
            stringy = stringFormat(stringy)
            data.append(stringy)
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        #A little different to the two functions above, as a list of skills needs to exported from the Skills table using the enemyID.
        #This demonstrates the need for a relational database for this application.
        skillList = getSkillsList(name, "Enemy")
        enemy = {"name": data[1], "act": data[2], "MHP": data[3], "MMP": data[4], "ATK": data[5], "DEF": data[6], "MAT": data[7], "MDF": data[8], "AGI": data[9], "LUK": data[10], "overview": data[11], "description": data[12], "img": data[14], "skillList": skillList}
        print(enemy)
        db.close()
        if address == 'Edit':
            return render_template('PageHTML/individEnemyEdit.html', name=enemy["name"], act=enemy["act"], MHP=enemy["MHP"], MMP=enemy["MMP"], ATK=enemy["ATK"], DEF=enemy["DEF"], MAT=enemy["MAT"], MDF=enemy["MDF"], AGI=enemy["AGI"], LUK=enemy["LUK"], overview=enemy["overview"], description=enemy["description"], img = enemy["img"], address=address)
        else:
            return render_template('PageHTML/individEnemyPage.html', name=enemy["name"], act=enemy["act"], MHP=enemy["MHP"], MMP=enemy["MMP"], ATK=enemy["ATK"], DEF=enemy["DEF"], MAT=enemy["MAT"], MDF=enemy["MDF"], AGI=enemy["AGI"], LUK=enemy["LUK"], overview=enemy["overview"], description=enemy["description"], img = enemy["img"], skillList = enemy["skillList"], address=address)

##A function used to retrieve a specific class's details from the database and display them using the IndividClass page template.
def accessClass(name, address):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM classes  WHERE classes.name = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            stringy = str(item)
            stringy = stringFormat(stringy)
            data.append(stringy)
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        #Needs a skill list like AccessEnemy().
        skillList = getSkillsList(name, "Class")
        classD = {"name": data[1], "sMHP": data[2], "sMMP": data[3], "sATK": data[4], "sDEF": data[5], "sMAT": data[6], "sMDF": data[7], "sAGI": data[8], "sLUK": data[9], "fMHP": data[10], "fMMP": data[11], "fATK": data[12], "fDEF": data[13], "fMAT": data[14], "fMDF": data[15], "fAGI": data[16], "fLUK": data[17], "overview": data[18], "description": data[19], "img": data[20], "skillList": skillList}
        print(classD)
        db.close()
        if address == 'Edit':
            return render_template('PageHTML/individClassEdit.html', name=classD["name"], baseMHP=classD["sMHP"], baseMMP=classD["sMMP"], baseATK=classD["sATK"], baseDEF=classD["sDEF"], baseMAT=classD["sMAT"], baseMDF=classD["sMDF"], baseAGI=classD["sAGI"], baseLUK=classD["sLUK"], maxMHP=classD["fMHP"], maxMMP=classD["fMMP"], maxATK=classD["fATK"], maxDEF=classD["fDEF"], maxMAT=classD["fMAT"], maxMDF=classD["fMDF"], maxAGI=classD["fAGI"], maxLUK=classD["fLUK"], overview=classD["overview"], description=classD["description"], img = classD["img"], address=address)
        else:
            return render_template('PageHTML/individClassPage.html', name = classD["name"], baseMHP = classD["sMHP"], baseMMP = classD["sMMP"], baseATK = classD["sATK"], baseDEF = classD["sDEF"], baseMAT = classD["sMAT"], baseMDF = classD["sMDF"], baseAGI = classD["sAGI"], baseLUK = classD["sLUK"], maxMHP = classD["fMHP"], maxMMP = classD["fMMP"], maxATK = classD["fATK"], maxDEF = classD["fDEF"], maxMAT = classD["fMAT"], maxMDF = classD["fMDF"], maxAGI = classD["fAGI"], maxLUK = classD["fLUK"], overview = classD["overview"], description = classD["description"], skillList=classD["skillList"], img = classD["img"], address=address)

##A function used to retrieve a specific party member's details from the database and display them using the IndividParty page template.
def accessMember(name, address):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM PartyMembers  WHERE PartyMembers.firstName = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            stringy = str(item)
            stringy = stringFormat(stringy)
            data.append(stringy)
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        skillList = getSkillsList(name, "Player")
        member = {"name": data[1] + " " + data[2], "firstName": data[1], "lastName": data[2], "startingLevel": data[3], "MHP": data[4], "MMP": data[5], "ATK": data[6], "DEF": data[7], "MAT": data[8], "MDF": data[9], "AGI": data[10], "LUK": data[11], "support1N": data[12], "support1L": data[13], "support2N": data[14], "support2L": data[15], "support3N": data[16], "support3L": data[17], "support4N": data[18], "support4L": data[19], "support5N": data[20], "support5L": data[21], "overview": data[22], "description": data[23], "img": data[26], "skillList": skillList}
        print(member)
        db.close()
        if address == 'Edit':
            return render_template('PageHTML/individPartyEdit.html', name=member["name"], firstName=member["firstName"], lastName=member["lastName"], level=member["startingLevel"], MHP=member["MHP"], MMP=member["MMP"], ATK=member["ATK"], DEF=member["DEF"], MAT=member["MAT"], MDF=member["MDF"], AGI=member["AGI"], LUK=member["LUK"], support1N=member["support1N"], support1L=member["support1L"], support2N=member["support2N"], support2L=member["support2L"], support3N=member["support3N"], support3L=member["support3L"], support4N=member["support4N"], support4L=member["support4L"], support5N=member["support5N"], support5L=member["support5L"], overview=member["overview"], description=member["description"], img = member["img"], address=address)
        else:
            return render_template('PageHTML/individPartyPage.html', name=member["name"], firstName=member["firstName"], lastName=member["lastName"], level = member["startingLevel"], MHP = member["MHP"], MMP = member["MMP"], ATK = member["ATK"], DEF = member["DEF"], MAT = member["MAT"], MDF = member["MDF"], AGI = member["AGI"], LUK = member["LUK"], support1N = member["support1N"], support1L = member["support1L"], support2N = member["support2N"], support2L = member["support2L"], support3N = member["support3N"], support3L = member["support3L"], support4N = member["support4N"], support4L = member["support4L"], support5N = member["support5N"], support5L = member["support5L"], overview = member["overview"], description = member["description"], img = member["img"],  skillList = member["skillList"], address=address)

##A function used to retrieve a specific location's details from the database and display them using the IndividLocation page template.
def accessLocation(name, address):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM locations  WHERE locations.name = ?"
    args = [name]
    for row in db.cursor().execute(sql, args):
        for item in row:
            stringy = str(item)
            stringy = stringFormat(stringy)
            data.append(stringy)
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        location = {"name": data[1], "act": data[2], "connect": data[3], "overview": data[4], "description": data[5], "img": data[6]}
        print(location)
        db.close()
        if address == 'Edit':
            return render_template('PageHTML/individLocationEdit.html', name=location["name"], act=location["act"], connect=location["connect"], overview=location["overview"], description=location["description"], img = location["img"], address=address)
        else:
            return render_template('PageHTML/individLocationPage.html', name = location["name"], act = location["act"], connect = location["connect"], overview = location["overview"], description = location["description"], img = location["img"], address=address)

##A function used to retrieve the data on the plot and display it on the PlotOverview page.
##Necessary to allow users to edit the plot.
def accessPlot(address):
    db = openDatabase()
    dbc = db.cursor()

    data = []
    sql = "SELECT * FROM plot WHERE plot.plotID = 1"
    for row in db.cursor().execute(sql):
        for item in row:
            stringy = str(item)
            stringy = stringFormat(stringy)
            data.append(stringy)
    print(data)
    print("\n")
    isNull = (data == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        plot = {"overview": data[1], "act1": data[2], "act2": data[3], "act3": data[4], "SeTa": data[5], "SeLu": data[6], "SeMa": data[7], "TaYl": data[8], "TaCl": data[9], "LuBr": data[10], "LuYl": data[11], "BrMa": data[12], "BrTa": data[13], "MaTa": data[14], "ClTa": data[15]}
        print(plot)
        db.close()
        if address == 'Edit':
            return render_template('PageHTML/plotEdit.html', overview=plot["overview"], actOne=plot["act1"], actTwo=plot["act2"], actThree=plot["act3"], SeTaEnding=plot["SeTa"], SeLuEnding=plot["SeLu"], SeMaEnding=plot["SeMa"], TaYlEnding=plot["TaYl"], TaClEnding=plot["TaCl"], LuBrEnding=plot["LuBr"], LuYlEnding=plot["LuYl"], BrMaEnding=plot["BrMa"], BrTaEnding=plot["BrTa"], MaTaEnding=plot["MaTa"], ClTaEnding=plot["ClTa"], address=address)
        else:
            return render_template('PageHTML/plotSummary.html', overview=plot["overview"], actOne=plot["act1"], actTwo=plot["act2"], actThree=plot["act3"], SeTaEnding=plot["SeTa"], SeLuEnding=plot["SeLu"], SeMaEnding=plot["SeMa"], TaYlEnding=plot["TaYl"], TaClEnding=plot["TaCl"], LuBrEnding=plot["LuBr"], LuYlEnding=plot["LuYl"], BrMaEnding=plot["BrMa"], BrTaEnding=plot["BrTa"], MaTaEnding=plot["MaTa"], ClTaEnding=plot["ClTa"], address=address)

##A function that retrieves and displays information on credits and contributions to the wiki; not really necessary as users cannot edit these,
##but it simply keeps all the information in one place, which seems more professional and tidy.
def accessCredits():
    db = openDatabase()
    dbc = db.cursor()

    dataName = []
    dataContributor = []
    sql = "SELECT * FROM contributors"
    for row in db.cursor().execute(sql):
        stringy = str(row[0])
        stringy = stringFormat(stringy)
        dataName.append(stringy)
        stringy = str(row[1])
        stringy = stringFormat(stringy)
        dataContributor.append(stringy)
    print(dataName)
    print("\n")
    print(dataContributor)
    print("\n")
    isNull = (dataName == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        db.close()
        return render_template('PageHTML/creditAndContributions.html', items=dataName, items2=dataContributor)

##A function used to retrieve all information stored on edits, which is generated (mainly) automatically when a user edits a page.
def accessEdits():
    db = openDatabase()
    dbc = db.cursor()

    dataPage = []
    dataDT = []
    dataChange = []
    sql = "SELECT * FROM edits"
    for row in db.cursor().execute(sql):
        stringy = str(row[1])
        stringy = stringFormat(stringy)
        dataPage.append(stringy)
        stringy = str(row[2])
        stringy = stringFormat(stringy)
        dataDT.append(stringy)
        stringy = str(row[3])
        stringy = stringFormat(stringy)
        dataChange.append(stringy)
    print(dataPage)
    print("\n")
    print(dataDT)
    print("\n")
    print(dataChange)
    print("\n")
    isNull = (dataChange == [])
    print(isNull)
    print("\n")
    if isNull:
        return accessPageNotFound()
    else:
        db.close()
        return render_template('PageHTML/editLog.html', items=dataPage, items2=dataDT, items3=dataChange)


#A giant function that handles retrieving and displaying information for all 'ListPages' on the website,
##i.e. those that display all the characters/skills/enemies/etc.
def loadList(tableName):
    db = openDatabase()
    dbc = db.cursor()
    data = []
    ###Characters Section:
    #Divided into three sections using character type.
    if tableName == "Characters":
        sql = "SELECT Characters.firstName, Characters.surname FROM Characters WHERE Characters.type = 'Enemy'"
        foeFNData = []
        foeLNData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row[0])
            stringy = stringFormat(stringy)
            foeFNData.append(stringy)
            stringy = " " + str(row[1])
            stringy = stringFormat(stringy)
            foeLNData.append(stringy)
        print(foeFNData)
        print(foeLNData)
        print("\n")
        foeTData = ''.join(foeFNData + foeLNData)
        print(foeTData)

        sql = "SELECT Characters.firstName, Characters.surname FROM Characters WHERE Characters.type = 'Playable'"
        playFNData = []
        playLNData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row[0])
            stringy = stringFormat(stringy)
            playFNData.append(stringy)
            stringy = " " + str(row[1])
            stringy = stringFormat(stringy)
            playLNData.append(stringy)
        print(playFNData)
        print(playLNData)
        print("\n")
        playTData = ''.join(playFNData + playLNData)
        print(playTData)

        sql = "SELECT Characters.firstName, Characters.surname FROM Characters WHERE Characters.type = 'NPC'"
        npcFNData = []
        npcLNData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row[0])
            stringy = stringFormat(stringy)
            npcFNData.append(stringy)
            stringy = " " + str(row[1])
            stringy = stringFormat(stringy)
            npcLNData.append(stringy)
        print(npcFNData)
        print(npcLNData)
        print("\n")
        npcTData = ''.join(npcFNData + npcLNData)
        print(npcTData)
        return render_template('PageHTML/charList.html', playableFNTable = playFNData, playableLNTable = playLNData, enemyFNTable = foeFNData, enemyLNTable = foeLNData, npcFNTable = npcFNData, npcLNTable = npcLNData)

    ###Classes Section:
    elif tableName == "Classes":
        sql = "SELECT Classes.name FROM Classes"
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            data.append(stringy)
        print(data)
        print("\n")
        tableData = ' '.join(data)
        print(tableData)
        return render_template('PageHTML/classList.html', tableData = data)

    ###Enemies Section:
    elif tableName == "Enemies":
        sql = "SELECT Enemies.name FROM Enemies"
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            data.append(stringy)
        print(data)
        print("\n")
        tableData = ''.join(data)
        print(tableData)
        return render_template('PageHTML/enemyList.html', tableData = data)

    ###Equipment Section:
    #Probably the most complicated of the list types.
    elif tableName == "Equipment":
        sql = "SELECT Equipment.name, Equipment.type, Equipment.atk, Equipment.def, Equipment.mat, Equipment.mdf, Equipment.agi, Equipment.luk, Equipment.extraEff FROM Equipment WHERE Equipment.slot = 'Weapon'"
        weaponData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            weaponData.append(stringy)
        print(data)
        print("\n")
        weaponTData = ''.join(weaponData)
        print(weaponTData)

        sql = "SELECT Equipment.name, Equipment.type, Equipment.atk, Equipment.def, Equipment.mat, Equipment.mdf, Equipment.agi, Equipment.luk, Equipment.extraEff FROM Equipment WHERE Equipment.slot = 'Armour'"
        armourData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            armourData.append(stringy)
        print(armourData)
        print("\n")
        armourTData = ''.join(armourData)
        print(armourTData)

        sql = "SELECT Equipment.name, Equipment.type, Equipment.atk, Equipment.def, Equipment.mat, Equipment.mdf, Equipment.agi, Equipment.luk, Equipment.extraEff FROM Equipment WHERE Equipment.slot = 'Accessory'"
        accData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            accData.append(stringy)
        print(accData)
        print("\n")
        accTData = ''.join(accData)
        print(accTData)

        sql = "SELECT Equipment.name, Equipment.type, Equipment.atk, Equipment.def, Equipment.mat, Equipment.mdf, Equipment.agi, Equipment.luk, Equipment.extraEff FROM Equipment WHERE Equipment.slot = 'Spirit'"
        spiritData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            spiritData.append(stringy)
        print(spiritData)
        print("\n")
        spiritTData = ''.join(spiritData)
        print(spiritTData)
        return render_template('PageHTML/equipList.html', weaponTable = weaponData, armourTable = armourData, accTable = accData, spiritTable = spiritData)

    ###Locations Section:
    #These are divided by act of the story where they first appear.
    elif tableName == "Locations":
        sql = "SELECT Locations.name FROM Locations WHERE Locations.act = '1'"
        actIData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            actIData.append(stringy)
        print(actIData)
        print("\n")
        actITData = ''.join(actIData)
        print(actIData)

        sql = "SELECT Locations.name FROM Locations WHERE Locations.act = '2'"
        actIIData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            actIIData.append(stringy)
        print(actIIData)
        print("\n")
        actIITData = ''.join(actIIData)
        print(actIITData)

        sql = "SELECT Locations.name FROM Locations WHERE Locations.act = '3'"
        actIIIData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            actIIIData.append(stringy)
        print(actIIIData)
        print("\n")
        actIIITData = ''.join(actIIIData)
        print(actIIITData)

        sql = "SELECT Locations.name FROM Locations WHERE Locations.act = '4' OR Locations.act = '0'"
        actIVData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            actIVData.append(stringy)
        print(actIVData)
        print("\n")
        actIVTData = ''.join(actIVData)
        print(actIVTData)
        return render_template('PageHTML/locationList.html', act1Table = actIData, act2Table = actIIData, act3Table = actIIIData, act4Table = actIVData)

    ###Party Members Section:
    elif tableName == "PartyMembers":
        sql = "SELECT PartyMembers.firstName, PartyMembers.surname FROM PartyMembers"
        memberFNData = []
        memberLNData = []
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row[0])
            stringy = stringFormat(stringy)
            memberFNData.append(stringy)
            stringy = " " + str(row[1])
            stringy = stringFormat(stringy)
            memberLNData.append(stringy)
        print(memberFNData)
        print("\n")
        print(memberLNData)
        print("\n")
        tableData = ''.join(memberFNData + memberLNData)
        print(tableData)
        return render_template('PageHTML/partyList.html', tableFNData=memberFNData, tableLNData=memberLNData)

    ###Skills Section:
    elif tableName == "Skills":
        sql = "SELECT Skills.name FROM Skills"
        print(sql)
        print('\n')
        for row in db.cursor().execute(sql):
            stringy = str(row)
            stringy = stringFormat(stringy)
            data.append(stringy)
        print(data)
        print("\n")
        tableData = ''.join(data)
        print(tableData)
        db.close()
        return render_template('PageHTML/skillList.html', tableData=data)
    return accessPageNotFound()

###A function used as part of AccessMember and AccessEnemy to create a unique list of skills for that character.
def getSkillsList(name, type):
    db = openDatabase()
    dbc = db.cursor()
    skillIds = []
    skillList = []
    id = 0
    memberID = 0
    sql = ""
    #-Also used in AccessClass, this decision statement determines which type of page is accessing the functions,
    #then executes the correct query.
    if type == "Player":
        sql = "SELECT MemberID FROM PartyMembers WHERE PartyMembers.FirstName = ?"
        args = [name]
        for item in db.cursor().execute(sql, args):
            memberID = item
            print(item)
            print("\n")
        sql = "SELECT ClassID FROM PartyMembers WHERE PartyMembers.MemberID = ?"
        args = [memberID]
        for item in db.cursor().execute(sql, args[0]):
            if id == 0:
                id = item
        sql = "SELECT SkillID, Level FROM SkillToUser WHERE SkillToUser.ClassID = ?"

    elif type == "Class":
        sql = "SELECT ClassID FROM Classes WHERE Classes.Name = ?"
        args = [name]
        for item in db.cursor().execute(sql, args):
            id = item
            print(id)
            print("\n")
        sql = "SELECT SkillID, Level FROM SkillToUser WHERE SkillToUser.ClassID = ?"

    else:
        sql = "SELECT EnemyID FROM Enemies WHERE enemies.Name = ?"
        args = [name]
        for item in db.cursor().execute(sql, args):
            id = item
            print(id)
            print("\n")
        sql = "SELECT SkillID FROM SkillToUser WHERE SkillToUser.EnemyID = ?"

    for row in db.cursor().execute(sql,id):
        for item in row:
            strItem = [str(item)]
            sql2 = "SELECT Skills.Name FROM Skills, SkillToUser WHERE Skills.SkillId = ? AND Skills.SkillId = SkillToUser.SkillId"
            for line in db.cursor().execute(sql2, strItem):
                for index in row:
                    stringy = str(line)
                    stringy = stringFormat(stringy)
                    skillList.append(stringy)
            print("Skill List: ")
            print(skillList)
            print('\n')
    return skillList


###This function exports data from the Edit version of the unique class page to the database.
def submitClass(className, overview, imgString, name, owner, BaseMHP, BaseMMP, BaseATK, BaseDEF, BaseMAT, BaseMDF, BaseAGI, BaseLUK, MaxMHP, MaxMMP, MaxATK, MaxDEF, MaxMAT, MaxMDF, MaxAGI, MaxLUK, description):
    db = openDatabase()
    dbc = db.cursor()
    check = ""
    sql = "SELECT * FROM classes WHERE classes.skillName = ?"
    nameCheck = [className]
    print(nameCheck[0])
    for row in db.cursor().execute(sql, nameCheck):
        check = row
    isNull = (check == "")
    print(isNull)
    print("\n")
    if isNull:
        sql = "INSERT INTO skills (name, StartMHP, StartMHP, StartMMP, StartATK, StartDEF, StartMAT, StartMDF, StartAGI, StartLUK, FinalMHP, FinalMMP, FinalATK, FinalDEF, FinalMAT, FinalMDF, FinalAGI, FinalLUK, overview, description, img) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [name, BaseMHP, BaseMMP, BaseATK, BaseDEF, BaseMAT, BaseMDF, BaseAGI, BaseLUK, MaxMHP, MaxMMP, MaxATK, MaxDEF, MaxMAT, MaxMDF, MaxAGI, MaxLUK, overview, description, imgString]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Class Added!")
    else:
        sql = "UPDATE characters SET name = ?, StartMHP = ?, StartMHP = ?, StartMMP = ?, StartATK = ?, StartDEF = ?, StartMAT = ?, StartMDF = ?, StartAGI = ?, StartLUK = ?, FinalMHP = ?, FinalMMP = ?, FinalATK = ?, FinalDEF = ?, FinalMAT = ?, FinalMDF = ?, FinalAGI = ?, FinalLUK = ?, overview = ?, description = ?, img = ? WHERE name = ?"
        args = [name, BaseMHP, BaseMMP, BaseATK, BaseDEF, BaseMAT, BaseMDF, BaseAGI, BaseLUK, MaxMHP, MaxMMP, MaxATK, MaxDEF, MaxMAT, MaxMDF, MaxAGI, MaxLUK, overview, description, imgString, nameCheck[0]]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Class Updated!")
    return "Class Added/Updated Successfully"

###This function exports data from the Edit version of the unique skill page to the database.
def submitSkill(skillName, overview, imgString, name, skillType, usage, skillElement, description):
    db = openDatabase()
    dbc = db.cursor()
    check = ""
    sql = "SELECT * FROM skills WHERE skills.name = ?"
    nameCheck = [skillName]
    print(nameCheck[0])
    for row in db.cursor().execute(sql, nameCheck):
        check = row
    isNull = (check == "")
    print(isNull)
    print("\n")
    #Similar to the decision in submitChar, except like with most pages, this one uses the title to determine whether it is an update
    #or a new page; allowing for users to change skill names.
    if isNull:
        sql = "INSERT INTO skills (name, type, usage, element, overview, description, img) VALUES (?, ?, ?, ?, ?, ?, ?)"
        args = [name, skillType, usage, skillElement, overview, description, imgString]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Skill Added!")
    else:
        sql = "UPDATE skills SET name = ?, type = ?, usage = ?, element = ?, overview = ?, description = ?, img = ? WHERE skillName = ?"
        args = [name, skillType, usage, skillElement, overview, description, imgString, nameCheck[0]]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Skill Updated!")
    return "Skill Added/Updated Successfully"

###This function exports data from the Edit version of the unique character page to the database.
def submitCharacter(charName, overview, imgString, firstName, lastName, age, race, familyMembers, charType, location, description):
    db = openDatabase()
    dbc = db.cursor()
    check = ""
    sql = "SELECT * FROM characters WHERE characters.firstName = ?"
    nameCheck = [firstName]
    print(nameCheck[0])
    for row in db.cursor().execute(sql, nameCheck):
        check = row
    isNull = (check == "")
    print(isNull)
    print("\n")
    #Either adds the data as a new character or updates an existing one, depending on the first name again.
    if isNull:
        sql = "INSERT INTO characters (firstName, surname, age, race, family, type, location, overview, description, img) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [firstName, lastName, age, race, familyMembers, charType, location, overview, description, imgString]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Character Added!")
    else:
        sql = "UPDATE characters SET firstName = ?, surname = ?, age = ?, race = ?, family = ?, type = ?, location = ?, overview = ?, description = ?, img = ? WHERE firstName = ?"
        args = [firstName, lastName, age, race, familyMembers, charType, location, overview, description, imgString, nameCheck[0]]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Character Updated!")
    return "Character Added/Updated Successfully"

def submitMember(memberName, overview, imgString, firstName, lastName, memberClass, level, MHP, MMP, ATK, DEF, MAT, MDF, AGI, LUK, support1Name, support1Lv, support2Name, support2Lv, support3Name, support3Lv, support4Name, support4Lv, support5Name, support5Lv, description):
    db = openDatabase()
    dbc = db.cursor()
    check = ""
    sql = "SELECT * FROM partymembers WHERE partymembers.name = ?"
    nameCheck = [memberName]
    print(nameCheck[0])
    for row in db.cursor().execute(sql, nameCheck):
        check = row
    isNull = (check == "")
    print(isNull)
    print("\n")
    ###
    mClassID = 1
    if isNull:
        sql = "INSERT INTO partymembers (firstName, surname, classID, startingLevel, MHP, MMP, ATK, DEF, MAT, MDF, AGI, LUK, support1, support1Lv, support2, support2Lv, support3, support3Lv, support4, support4Lv, support5, support5Lv, overview, description, img) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [firstName, lastName, mClassID, level, MHP, MMP, ATK, DEF, MAT, MDF, AGI, LUK, support1Name, support1Lv, support2Name, support2Lv, support3Name, support3Lv, support4Name, support4Lv, support5Name, support5Lv, description, overview, imgString]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Party Member Added!")
    else:
        sql = "UPDATE partymembers SET firstName = ?, surname = ?, classID = ?, startingLevel = ?, MHP = ?, MMP = ?, ATK = ?, DEF = ?, MAT = ?, MDF = ?, AGI = ?, LUK = ?, support1 = ?, support1Lv = ?, support2 = ?, support2Lv = ?, support3 = ?, support3Lv = ?, support4 = ?, support4Lv = ?, support5 = ?, support5Lv = ?, overview = ?, description = ?, img = ? WHERE name = ?"
        args = [firstName, lastName, memberClass, level, MHP, MMP, ATK, DEF, MAT, MDF, AGI, LUK, support1Name, support1Lv, support2Name, support2Lv, support3Name, support3Lv, support4Name, support4Lv, support5Name, support5Lv, description, overview, imgString, nameCheck[0]]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Party Member Updated!")
    return "Party Member Added/Updated Successfully"

def submitEnemy(enemyName, overview, imgString, name, act, MHP, MMP, ATK, DEF, MAT, MDF, AGI, LUK, description):
    db = openDatabase()
    dbc = db.cursor()
    check = ""
    sql = "SELECT * FROM enemies WHERE enemies.name = ?"
    nameCheck = [enemyName]
    print(nameCheck[0])
    for row in db.cursor().execute(sql, nameCheck):
        check = row
    isNull = (check == "")
    print(isNull)
    print("\n")
    if isNull:
        sql = "INSERT INTO enemies (name, act, MHP, MMP, ATK, DEF, MAT, MDF, AGI, LUK, overview, description, img) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = [name, act, MHP, MMP, ATK, DEF, MAT, MDF, AGI, LUK, overview, description, imgString]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Enemy Added!")
    else:
        sql = "UPDATE enemies SET name = ?, act = ?, MHP = ?, MMP = ?, ATK = ?, DEF = ?, MAT = ?, MDF = ?, AGI = ?, LUK = ?, overview, description, img WHERE name = ?"
        args = [name, act, MHP, MMP, ATK, DEF, MAT, MDF, AGI, LUK, overview, description, imgString, nameCheck[0]]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Enemy Updated!")
    return "Enemy Added/Updated Successfully"

###This function exports data from the Edit version of the unique location page to the database.
def submitLocation(locName, overview, imgString, name, act, locType, locConnect, description):
    db = openDatabase()
    dbc = db.cursor()
    check = ""
    sql = "SELECT * FROM locations WHERE locations.name = ?"
    nameCheck = [locName]
    print(nameCheck[0])
    for row in db.cursor().execute(sql, nameCheck):
        check = row
    isNull = (check == "")
    print(isNull)
    print("\n")
    if isNull:
        sql = "INSERT INTO locations (name, act, type, connect, overview, description, img) VALUES (?, ?, ?, ?, ?, ?, ?)"
        args = [name, act, locType, locConnect, overview, description, imgString]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Character Added!")
    else:
        sql = "UPDATE locations SET name = ?, act = ?, type = ?, connect = ?, overview = ?, description = ?, img WHERE name = ?"
        args = [name, act, locType, locConnect, overview, description, imgString, nameCheck[0]]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Character Updated!")
    return "Character Added/Updated Successfully"

###This function exports data from the Edit version of the Plot page; always updating, since there is only one plot of Boundary of Shade and Future!
def submitPlot(overview, actOne, actTwo, actThree, SeTa, SeLu, SeMa, TaYl, TaCl, LuBr, LuYl, BrMa, BrTa, MaTa, ClTa):
    db = openDatabase()
    dbc = db.cursor()
    sql = "UPDATE plot SET overview = ?, actI = ?, actII = ?, EndST = ?, EndSL = ?, EndSM = ?, EndTY = ?, EndTC = ?, EndLB = ?, EndLY = ?, EndBM = ?, EndBT = ?, EndMT = ?, EndCT = ? WHERE plot.PlotID = 1"
    args = [overview, actOne, actTwo, actThree, SeTa, SeLu, SeMa, TaYl, TaCl, LuBr, LuYl, BrMa, BrTa, MaTa, ClTa]
    print(args)
    db.cursor().execute(sql, args)
    db.commit()
    return "Plot Added/Updated Successfully"


###This function retrieves the information needed for a wiki-edit's metadata, and exports this to the database.
###Also handles users forgetting to enter an 'editMessage' detailing the change made.
def generateEdit(editMessage, page):
    pageLink = page.replace("/edit", "")
    editTime = datetime.datetime.now()
    db = openDatabase()
    dbc = db.cursor()
    messageNull = (editMessage == "")
    pageNull = (page == "")
    print("\n")
    print(messageNull)
    print(pageNull)
    print("\n")
    #Probably not the best way of managing this, but it was sufficient during testing, which is enough for now.
    if messageNull == True or pageNull == True:
        #Run this function before adding data, then abort outer process if no message exists, show error message asking for message, then return user to the page they were on (or rather, give them control back, since they're already on the page).
        return False
    else:
        sql = "INSERT INTO Edits (page, datentime, change) VALUES (?, ?, ?)"
        args = [page, editTime, editMessage]
        print(args)
        db.cursor().execute(sql, args)
        db.commit()
        print("Edit Added!")
        return True

###Never used; just a stub function during development.
def submitPage():
    return render_template('TemplateHTML/Homepage.html')

###A function used when displaying data exported from the database, since the formatting is weird.
def stringFormat(stringy):
    #Remove strange symbols added by SQLite during transfer (possibly due to the use of dictionaries?)
    stringy = stringy.replace("(", "")
    stringy = stringy.replace(")", "")
    stringy = stringy.replace("'", "")
    stringy = stringy.replace('"', '')
    stringy = stringy.replace(",", "")
    #Create line breaks where <br> is found.
    print(stringy)
    stringy = stringy.replace("<br>", "\n")
    print(stringy)
    #Successfully removes '<br>', but the line breaks don't work.
    return stringy


###This function renders the Error 404 page for Regnella Wiki; created to prevent code duplication.
def accessPageNotFound(error):
    print("Page not found!")
    return render_template('PageHTML/PageNotFound.html')

###This function renders the Error 50X page for Regnella Wiki; created to prevent code duplication.
def accessEditingError(error):
    print("Could not add data to database!")
    return render_template('PageHTML/EditingError.html')
