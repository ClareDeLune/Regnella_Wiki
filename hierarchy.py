###Set-Up
from python.globalFunctions import *

app = Flask(__name__)


###LEVEL NO. 1
#Homepage Nav.
@app.route('/')
@app.route('/home')
def home():
    return render_template('TemplateHTML/Homepage.html')

###LEVEL NO. 2
#PlotOverview Nav.
@app.route('/home/PlotOverview')
@app.route('/home/Plot-Overview')
@app.route('/home/plot-overview')
@app.route('/home/plotoverview')
def plotOverview():
    return render_template('PageHTML/plotSummary.html')

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
    return render_template('PageHTML/skillList.html')


#EnemiesPage Nav.
@app.route('/home/Enemies')
@app.route('/home/enemies')
def enemiesPage():
    return render_template('PageHTML/enemyList.html')


#CharactersPage Nav.
@app.route('/home/Characters')
@app.route('/home/characters')
def charactersPage():
    return render_template('PageHTML/charList.html')


#PartyMembersPage Nav.
@app.route('/home/Party-Members')
@app.route('/home/party-members')
@app.route('/home/PartyMembers')
@app.route('/home/partymembers')
def partyMembers():
    return render_template('PageHTML/partyList.html')


#ClassesPage Nav.
@app.route('/home/Classes')
@app.route('/home/classes')
def classesPage():
    return render_template('PageHTML/classList.html')


#EquipmentPage Nav.
@app.route('/home/Equipment')
@app.route('/home/equipment')
def equipmentPage():
    return render_template('PageHTML/equipList.html')


#LocationsPage Nav.
@app.route('/home/Locations')
@app.route('/home/locations')
def locPage():
    return render_template('PageHTML/locationList.html')


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
    return render_template('PageHTML/creditAndContributions.html')


###LEVEL NO. 3
#Skill Nav.
@app.route('/home/Skills/Skill/<name>')
@app.route('/home/skills/skill/<name>')
def skill(name=None):
    sName = name
    accessSkill(name)


#Enemy Nav.
@app.route('/home/Enemies/<name>')
def enemy(name=None):
    sName = name
    accessEnemy(name)


#Character Nav.
@app.route('/home/Characters/<name>')
@app.route('/home/characters/<name>')
def character(name=None):
    sName = name
    return accessChar(sName)

#Member Nav.
@app.route('/home/Party-Members/<name>')
@app.route('/home/party-members/<name>')
@app.route('/home/PartyMembers/<name>')
@app.route('/home/partymembers/<name>')
def partyMember(name=None):
    sName = name
    accessMember(name)


#Class Nav.
@app.route('/home/Classes/<name>')
@app.route('/home/classes/<name>>')
def classFunc(name=None):
    sName = name
    accessClass(name)


#Location Nav.
@app.route('/home/Locations/<name>')
@app.route('/home/locations/<name>>')
def locationFunc(name=None):
    sName = name
    accessLocation(name)
'''
'''

###Happy Ending :)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
