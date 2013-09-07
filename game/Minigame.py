'''
Created on Sep 7, 2013

@author: Phillip
'''

from game.Question import Question
from game.Key import Key

class Minigame(object):
    '''
    classdocs
    '''

    def __init__(self,identifier="",question=None,key=None,answers=list(),numRetries=0):
        '''
        Constructor
        '''
        self.id = identifier
        self.setQuestion(question)
        self.setKey(key)
        self.answers = answers
        self.parent = None
        self.numRetries = numRetries
        
    def setKey(self, key):
        if key == None:
            return
        key.parent = self
        self.key = key
        
    def setQuestion(self, question):
        if question == None:
            return
        question.parent = self
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
                