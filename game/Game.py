'''
Created on Sep 6, 2013

@author: Phillip
'''

class Game(object):
    '''
    classdocs
    '''

    def __init__(self, admins = list(), users = list(), minigames = dict()):
        self.admins = list()
        self.users = list()
        self.minigames = dict()
        for admin in admins:
            self.addAdmin(admin)
        for user in users:
            self.addUser(user)
        for minigame in minigames.values():
            self.addMinigame(minigame)
    
    def addUser(self, user):
        self.users.append(user)
        
    def addAdmin(self, admin):
        self.admins.append(admin)
        
    def addMinigame(self, minigame):
        minigame.parent = self
        self.minigames[minigame.id] = minigame
        
    def notifyUsers(self, msg):
        for user in self.users:
            user.sendEmail(msg)
            
    def notifyAdmins(self, msg):
        for admin in self.admins:
            admin.sendEmail(msg)
            
    def notifyAll(self, msg):
        self.notifyAdmins(msg)
        self.notifyUsers(msg)
        
    def checkAnswer(self, minigameId, answer):
        if self.minigames.has_key(minigameId):
            mg = self.minigames.get(minigameId);
            if mg.canAnswer(answer.owner):
                return mg.verify(answer)
            else:
                return False;
        else:
            return False;
        
        