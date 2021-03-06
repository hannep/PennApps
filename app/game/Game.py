'''
Created on Sep 6, 2013

@author: Phillip
'''

import datetime
from User import User
from Admin import Admin
from Minigame import Minigame
from google.appengine.ext import ndb

class GameModel(ndb.Model):
    id = ndb.IntegerProperty()
    name = ndb.StringProperty()
    description = ndb.StringProperty()
    duration = ndb.IntegerProperty()
class Game(object):
    '''
    classdocs
    '''
    def __init__(self, name, admins = list(), users = list(), minigames = list(), duration = -1, description = ""):
        self.name = name
        self.description = description
        self.admins = list()
        self.users = list()
        self.adminNotifications = list()
        self.userNotifications = list()
        self.handGradedAnswers = list()
        self.answersGraded = list()
        self.minigames = dict()
        self.duration = duration
        self.start = datetime.datetime.now()
        for admin in admins:
            self.addAdmin(admin)
        for user in users:
            self.addUser(user)
        for minigame in minigames:
            self.addMinigame(minigame)
    def userHasCompleted(self, minigame, number):
        user = None
        for usr in self.users:
            if usr.phone == number:
                user = usr
        if user == None:
            return False
        try:
            user.completedMinigames[minigame]
            return True
        except:
            return False    
    def sortUsersByScore(self):
        return sorted(self.users, key=lambda x: x.getScore(), reverse=True)
    
    def addUser(self, user):
        self.users.append(user)
    
    def gradeHandGradedAnswer(self, answer, value):
        remove = None
        for ans in self.handGradedAnswers:
            if ans == answer:
                answer.grade(value)
                answer.markCompleted()
                remove = ans
        self.handGradedAnswers.remove(remove)
        self.answersGraded(answer)
        for user in self.users:
            if user == answer.owner:
                if value > 0:
                    user.sendText("Your answer was graded correct")
                else:
                    user.sendText("Your answer was graded incorrect")   
        pass 
    
    def addHandGradedAnswer(self, answer):
        self.notifyAdmins("An answer needs grading.")
        self.handGradedAnswers.append(answer)
        
    def addAdmin(self, admin):
        self.admins.append(admin)
        
    def addMinigame(self, minigame):
        minigame.parent = self
        self.minigames[minigame.id] = minigame
        
    def notifyUsers(self, msg):
        for user in self.users:
            user.sendEmail(msg)
            user.sendText(msg)
            self.userNotifications.append(msg)
            
    def notifyAdmins(self, msg):
        for admin in self.admins:
            admin.sendEmail(msg)
            admin.sendText(msg)
            self.adminNotifications.append(msg)
            
    def notifyAll(self, msg):
        self.notifyAdmins(msg)
        self.notifyUsers(msg)
        
    def isGameActive(self):
        if self.duration < 0:
            return True
        now = datetime.datetime.now()
        return (now - self.start).total_seconds() < self.duration
        
    def checkAnswer(self, minigameId, answer):
        if self.minigames.has_key(minigameId):
            mg = self.minigames.get(minigameId);
            if mg.canAnswer(answer.owner):
                return mg.verify(answer)
            else:
                return False
        else:
            return False
        
    @staticmethod
    def createFromAppEngine(id):
        users = User.createFromAppEngine()
        admins = Admin.createFromAppEngine()
        minigames = Minigame.createFromAppEngine()
        game_query = GameModel.query(GameModel.id == id)
        game = game_query.fetch(1)
        return Game(id, game[0].name, game[0].description, admins, users, minigames, game[0].duration) if len(game) > 0 else None
