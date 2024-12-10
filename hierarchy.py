###Set-Up
from python.globalFunctions import *

app = Flask(__name__)


###LEVEL NO. 1
#Homepage Nav.
@app.route('/')
@app.route('/home')
def home():
    return render_template('TemplateHTML/Homepage.html')

@app.route('/home/submit')
def submit(address='None'):
    return submitPage()

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
@app.route('/home/Skills/Edit/<name>')
@app.route('/home/skills/edit/<name>')
def skillEdit(name=None):
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
@app.route('/home/Characters/Edit/<name>')
@app.route('/home/characters/edit/<name>')
def charEdit(name=None):
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
@app.route('/home/Classes/Edit/<name>')
@app.route('/home/classes/edit/<name>')
def classEdit(name=None):
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
