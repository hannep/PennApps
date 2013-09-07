from game.Admin import Admin
from game.User import User
from game.Question import Question
from game.TextQuestion import TextQuestion
from game.TextKey import TextKey
from game.Minigame import Minigame
from game.Game import Game
from game.Answer import Answer
import fileinput, sys


admins = list()
admin = Admin("phroph@yahoo.com", "802-279-7097", "Phillip Huff")
admins.append(admin)

users = list()
user = User("johndoe@gmail.com", "867-5309", "John Doe")
users.append(user)

answers = ["blue, no yellow","blue","yellow"]

question = TextQuestion("What is your favorite color?")

value = 5

key = TextKey(answers, value)

minigames = dict()
minigame = Minigame("Monty-Python", question, key, list(), 0)
minigames[minigame.id] = minigame

game = Game(admins, users, minigames)

print "Question: " + minigame.id + "\n" + minigame.question.getTextRepresentation()
line = sys.stdin.readline()
answer = Answer(user, minigame.id, line[:-2])
if game.checkAnswer(minigame.id, answer):
    print "Correct answer.\n"
    sys.exit()
else:
    print "Incorrect answer.\n"
    sys.exit()