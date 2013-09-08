from Admin import *
from User import *
from Question import *
from TextQuestion import *
from TextKey import *
from Minigame import *
from Game import *
from Answer import *
from time import sleep
import fileinput, sys

def loadSampleData():
    game = GameModel(id = 0, duration = -1, name="game")
    game.put()
    
    admin = AdminModel(phone = "+18022797097", email = "phroph@yahoo.com", name = "Phillip Huff")
    admin.put()
    
    user = UserModel(phone = "867-5309", email="", name="Team Awesome")
    user.put()
    
    key = TextKeyModel(id = "testK", value = 5, answers = ["blue", "yellow"],
                       first = 5, second = 3, third = 1)
    key.put()
    
    minigame = MinigameModel(id = "Monty-Python", questionId="testQ", keyId="testK", key_type = "text", question_type="text", retries=0)
    minigame.put()
    
    question = TextQuestionModel(string = "What is your favorite color?", id = "testQ")
    question.put()

#loadSampleData()

sleep(1)

game = Game.createFromAppEngine(0)
if game == None:
    print "Game not found."
    sys.exit()
print "Users:\n"
for user in game.users:
    print user.name + " (" + user.email + "): " + user.phone + "\n"
print "Admins:\n"
for admin in game.admins:
    print admin.name + " (" + admin.email + "): " + admin.phone + "\n"
print "Minigames:\n"
for minigame in game.minigames.values():
    print minigame.id + ": " + minigame.question.getTextRepresentation() + " (" + str(minigame.key.answers) + ")\n"
