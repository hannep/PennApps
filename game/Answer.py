'''
Created on Sep 7, 2013

@author: Phillip
'''

class Answer(object):
    '''
    classdocs
    '''


    def __init__(self, owner, minigameId, textData = ""):
        '''
        Constructor
        '''
        self.owner = owner
        self.score = 0
        self.isGraded = False
        self.isComplete = False
        self.textData = textData
        self.id = minigameId
        
    def markCompleted(self):
        self.isComplete = True
        self.owner.completedMinigames[self.id] = self
        
    def markGraded(self):
        self.isGraded = True
        