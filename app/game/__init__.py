from Admin import *
from User import *
from Question import *
from TextQuestion import *
from TextKey import *
from Minigame import *
from Game import *
from Answer import *
import fileinput, sys
# import geopy
# import geopy.distance

game = GameModel(id = "game", duration = -1)
game.put()

admin = AdminModel(phone = "802-279-7097", email = "phroph@yahoo.com", name = "Phillip Huff")
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

game = Game.createFromAppEngine("game")
print "Users:\n"
for user in game.users:
    print user.name + " (" + user.email + "): " + user.phone + "\n"
print "Admins:\n"
for admin in game.admins:
    print admin.name + " (" + admin.email + "): " + admin.phone + "\n"
print "Minigames:\n"
for minigame in game.minigames.values():
    print minigame.id + ": " + minigame.question.getTextRepresentation() + " (" + str(minigame.key.answers) + ")\n"
#admins = list()
#admin = Admin("phroph@yahoo.com", "802-279-7097", "Phillip Huff")
#admins.append(admin)

#users = list()
#user = User("867-5309", "John Doe")
#users.append(user)

#answers = ["blue, no yellow","blue","yellow", "blue no yellow"]

#question = TextQuestion("What is your favorite color?")

#value = 5

#key = TextKey(answers, value)

#minigames = dict()
#minigame = Minigame("Monty-Python", question, key, list(), 0)
#minigames[minigame.id] = minigame

#game = Game(admins, users, minigames)

#print "Question: " + minigame.id + "\n" + minigame.question.getTextRepresentation()
#line = sys.stdin.readline()
#answer = Answer(user, minigame.id, line[:-2])
#if game.checkAnswer(minigame.id, answer):
#    print "Correct answer.\n"
#    sys.exit()
#else:
#    print "Incorrect answer.\n"
#    sys.exit()