###Set-Up
from crypt import methods

from python.globalFunctions import *

app = Flask(__name__)


###LEVEL NO. 1
#Homepage Nav.
@app.route('/')
@app.route('/home')
def home():
    return render_template('TemplateHTML/Homepage.html')

'''@app.route('/home/submit', methods=['GET', 'POST'])
def submit(address='None'):
    return submitPage()'''


###LEVEL NO. 2
#PlotOverview Nav.
@app.route('/home/PlotOverview')
@app.route('/home/Plot-Overview')
@app.route('/home/plot-overview')
@app.route('/home/plotoverview')
def plotOverview():
    address = 'plotEdit'
    return accessPlot(address)

#ForumPage Nav.
@app.route('/home/Forum-Page')
@app.route('/home/forum-page')
@app.route('/home/forumpage')
@app.route('/home/ForumPage')
def forumPage():
    return render_template('PageHTML/forumPage.html')


#SkillsPage Nav.
@app.route('/home/Skills')
@app.route('/home/skills')
def skillsPage():
    return loadList('Skills')


#EnemiesPage Nav.
@app.route('/home/Enemies')
@app.route('/home/enemies')
def enemiesPage():
    return loadList('Enemies')


#CharactersPage Nav.
@app.route('/home/Characters')
@app.route('/home/characters')
def charactersPage():
    return loadList("Characters")


#PartyMembersPage Nav.
@app.route('/home/Party-Members')
@app.route('/home/party-members')
@app.route('/home/PartyMembers')
@app.route('/home/partymembers')
def partyMembers():
    return loadList('PartyMembers')


#ClassesPage Nav.
@app.route('/home/Classes')
@app.route('/home/classes')
def classesPage():
    return loadList('Classes')


#EquipmentPage Nav.
@app.route('/home/Equipment')
@app.route('/home/equipment')
def equipmentPage():
    return loadList('Equipment')


#LocationsPage Nav.
@app.route('/home/Locations')
@app.route('/home/locations')
def locPage():
    return loadList('Locations')


#EditsPage Nav.
@app.route('/home/Edits-Log')
@app.route('/home/edits-log')
@app.route('/home/editslog')
@app.route('/home/EditsLog')
def editLog():
    return render_template('PageHTML/editLog.html')


#Credit&Contribution Nav.
@app.route('/home/Credits')
@app.route('/home/credits')
def credits():
    return accessCredits()


###LEVEL NO. 3
#Skill Nav.
@app.route('/home/Skills/<name>')
@app.route('/home/skills/<name>')
def skill(name=None):
    sName = name
    address = 'skillEdit'
    return accessSkill(name, address)

#Enemy Nav.
@app.route('/home/Enemies/<name>')
@app.route('/home/enemies/<name>')
def enemy(name=None):
    sName = name
    address = 'enemyEdit'
    return accessEnemy(name, address)


#Character Nav.
@app.route('/home/Characters/<name>')
@app.route('/home/characters/<name>')
def character(name=None):
    sName = name
    address = 'charEdit'
    return accessChar(name, address)

#Member Nav.
@app.route('/home/Party-Members/<name>')
@app.route('/home/party-members/<name>')
@app.route('/home/PartyMembers/<name>')
@app.route('/home/partymembers/<name>')
def partyMember(name=None):
    sName = name
    address = 'memberEdit'
    return accessMember(name, address)


#Class Nav.
@app.route('/home/Classes/<name>')
@app.route('/home/classes/<name>')
def classFunc(name=None):
    sName = name
    address = 'classEdit'
    return accessClass(name, address)


#Location Nav.
@app.route('/home/Locations/<name>')
@app.route('/home/locations/<name>')
def locationFunc(name=None):
    sName = name
    address = 'locationEdit'
    return accessLocation(name, address)


###LEVEL NO. 4
###Skill Edit:
@app.route('/home/Skills/Edit/<name>', methods=['GET', 'POST'])
@app.route('/home/skills/edit/<name>', methods=['GET', 'POST'])
def skillEdit(name=None):
    if request.method == 'POST':
        print("correct branch")
        print("\n")
        skillName = request.form.get('skillName')
        overview = request.form.get('overview')
        imgString = request.form.get('imgString')
        name = request.form.get('name')
        skillType = request.form.get('skillType')
        usage = request.form.get('usage')
        skillElement = request.form.get('skillElement')
        description = request.form.get('description')
        print("requests made:")
        print("\n")
        print(skillName)
        print(usage)
        print(overview)
        print("\n")
        submitSkill(skillName, overview, imgString, name, skillType, usage, skillElement, description)
        return loadList("Skills")
    else:
        sName = name
        address = 'Edit'
        return accessSkill(name, address)

###Enemy Edit:
@app.route('/home/Enemies/Edit/<name>')
@app.route('/home/enemies/edit/<name>')
def enemyEdit(name=None):
    sName = name
    address = 'Edit'
    return accessEnemy(name, address)


#Character Edit:
@app.route('/home/Characters/Edit/<name>', methods = ['GET', 'POST'])
@app.route('/home/characters/edit/<name>', methods=['GET', 'POST'])
def charEdit(name=None):
    if request.method == 'POST':
        print("correct branch")
        print("\n")
        charName = request.form.get('charName')
        overview = request.form.get('overview')
        imgString = request.form.get('imgString')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        age = request.form.get('age')
        race = request.form.get('race')
        familyMembers = request.form.get('familyMembers')
        charType = request.form.get('charType')
        location = request.form.get('location')
        description = request.form.get('description')
        print("requests made:")
        print("\n")
        print(charName)
        print(age)
        print(overview)
        print("\n")
        submitCharacter(charName, overview, imgString, firstName, lastName, age, race, familyMembers, charType, location, description)
        return loadList("Characters")
    else:
        sName = name
        address = 'Edit'
        return accessChar(name, address)

#Member Edit:
@app.route('/home/Party-Members/Edit/<name>')
@app.route('/home/party-members/edit/<name>')
@app.route('/home/PartyMembers/Edit/<name>')
@app.route('/home/partymembers/edit/<name>')
def partyMemberEdit(name=None):
    sName = name
    address = 'Edit'
    return accessMember(name, address)


#Class Edit:
@app.route('/home/Classes/Edit/<name>', methods = ['GET', 'POST'])
@app.route('/home/classes/edit/<name>', methods = ['GET', 'POST'])
def classEdit(name=None):
    if request.method == 'POST':
        print("correct branch")
        print("\n")
        className = request.form.get('className')
        overview = request.form.get('overview')
        imgString = request.form.get('imgString')
        name = request.form.get('name')
        owner = request.form.get('owner')
        BaseMHP = request.form.get('BaseMHP')
        BaseMMP = request.form.get('BaseMMP')
        BaseATK = request.form.get('BaseATK')
        BaseDEF = request.form.get('BaseDEF')
        BaseMAT = request.form.get('BaseMAT')
        BaseMDF = request.form.get('BaseMDF')
        BaseAGI = request.form.get('BaseAGI')
        BaseLUK = request.form.get('BaseLUK')
        MaxMHP = request.form.get('MaxMHP')
        MaxMMP = request.form.get('MaxMMP')
        MaxATK = request.form.get('MaxATK')
        MaxDEF = request.form.get('MaxDEF')
        MaxMAT = request.form.get('MaxMAT')
        MaxMDF = request.form.get('MaxMDF')
        MaxAGI = request.form.get('MaxAGI')
        MaxLUK = request.form.get('MaxLUK')
        description = request.form.get('description')
        print("requests made:")
        print("\n")
        print(name)
        print(MaxMHP)
        print(overview)
        print("\n")
        submitClass(className, overview, imgString, name, owner, BaseMHP, BaseMMP, BaseATK, BaseDEF, BaseMAT, BaseMDF, BaseAGI, BaseLUK, MaxMHP, MaxMMP, MaxATK, MaxDEF, MaxMAT, MaxMDF, MaxAGI, MaxLUK, description)
        return loadList("Classes")
    else:
        sName = name
        address = 'Edit'
        return accessClass(name, address)


#Location Edit:
@app.route('/home/Locations/Edit/<name>')
@app.route('/home/locations/edit/<name>')
def locationEdit(name=None):
    sName = name
    address = 'Edit'
    return accessLocation(name, address)

@app.route('/home/PlotOverview/Edit')
@app.route('/home/Plot-Overview/Edit')
@app.route('/home/plot-overview/edit')
@app.route('/home/plotoverview/edit')
def plotEdit():
    address = 'Edit'
    return accessPlot(address)

'''
'''

###Happy Ending :)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
