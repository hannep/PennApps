'''
Created on Sep 7, 2013

@author: Phillip
'''

from Person import Person

from google.appengine.ext import ndb

class UserModel(ndb.Model):
    phone = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    name = ndb.StringProperty(indexed=False)

class User(Person):
    '''
    classdocs
    '''


    def __init__(self, phone, name, email = ""):
        '''
        Constructor
        '''
        super(User,self).__init__(email, phone, name)
        self.completedMinigames = dict()
    
    def getScore(self):
        counter = 0
        for answer in self.completedMinigames.values():
            counter = counter + answer.score
        return counter
    
    def getNumCompletedPuzzles(self):
        counter = 0
        for answer in self.completedMinigames.values():
            if answer.isComplete:
                counter = counter + 1
        return counter
        
    @staticmethod
    def createFromAppEngine():
        user_query = UserModel.query()
        user_list = user_query.fetch()
        users = list()
        for user in user_list:
            users.append(User(user.phone, user.name, user.email))
        return users