'''
Created on Sep 7, 2013

@author: Phillip
'''

class Answer(object):
    '''
    classdocs
    '''


    def __init__(self, owner, minigameId, data = None):
        '''
        Constructor
        '''
        self.owner = owner
        self.score = 0
        self.isGraded = False
        self.isComplete = False
        self.data = data
        self.id = minigameId
        
    def markCompleted(self):
        self.isComplete = True
        self.owner.completedMinigames[self.id] = self
        
    def markGraded(self):
        self.isGraded = True
        
    def grade(self, grade):
        self.score = grade
        self.markGrade()