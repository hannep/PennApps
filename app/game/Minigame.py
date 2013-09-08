'''
Created on Sep 7, 2013

@author: Phillip
'''

from TextKey import TextKey
from LocationKey import LocationKey
from TextQuestion import TextQuestion
from ImageQuestion import ImageQuestion
from CompositeQuestion import CompositeQuestion
from google.appengine.ext import ndb

class MinigameModel(ndb.Model):
    id = ndb.StringProperty()
    questionId = ndb.StringProperty()
    keyId = ndb.StringProperty()
    key_type = ndb.StringProperty()
    question_type = ndb.StringProperty()
    retries = ndb.IntegerProperty()

class Minigame(object):
    '''
    classdocs
    '''

    def __init__(self, name, answer, question=None, answers=list(), numRetries=0):
        '''
        Constructor
        '''
        self.name = name
        self.answer = answer
        self.question = None
        self.setQuestion(question)
        self.answers = answers
        self.numRetries = numRetries
        
    def setKey(self, key):
        if key == None:
            return
        key.parent = self
        self.key = key
        
    def setQuestion(self, question):
        if question == None:
            return
        self.question = question
        
    def hasCompleted(self, user):
        for answer in self.answers:
            if answer.owner == user and answer.isComplete:
                return True
        return False
    
    def verify(self, answer):
        if self.key.isHandGraded:
            self.parent.notifyAdmins("An answer needs grading.")
        else:
            self.key.gradeAnswer(answer)
        self.answers.append(answer)
        return answer.isComplete
    
    def canAnswer(self, user):
        counter = 0
        for answer in self.answers:
            if answer.owner == user:
                counter = counter + 1
        return (counter - 1) < self.numRetries
    
    def countCorrectSolutions(self):
        counter = 0
        for answer in self.answers:
            if answer.isComplete:
                counter = counter + 1
        return counter
    
    @staticmethod
    def createFromAppEngine():
        minigame_query = MinigameModel.query()
        minigame_list = minigame_query.fetch();
        minigames = list()
        for minigame in minigame_list:
            key = None
            question = None
            if minigame.key_type.lower() == "text":
                key = TextKey.createFromAppEngine(minigame.keyId)
            elif minigame.key_type.lower() == "location":
                key = LocationKey.createFromAppEngine(minigame.keyId)
            elif minigame.key_type.lower() == "composite":
                pass
            if minigame.question_type.lower() == "text":
                question = TextQuestion.createFromAppEngine(minigame.questionId)
            elif minigame.question_type.lower() == "image":
                question = ImageQuestion.createFromAppEngine(minigame.questionId)
            elif minigame.question_type.lower() == "composite":
                question = CompositeQuestion.createFromAppEngine(minigame.questionId)
            minigames.append(Minigame(minigame.id, question, key, list(), minigame.retries))
        return minigames
                