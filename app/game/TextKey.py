'''
Created on Sep 7, 2013

@author: Phillip
'''

from game.Key import Key

class TextKey(Key):
    '''
    classdocs
    '''


    def __init__(self, answers, value):
        '''
        Constructor
        '''
        super(TextKey, self).__init__()
        self.answers = answers
        self.value = value
        
    def gradeAnswer(self, answer):
        for candidate in self.answers:
            if candidate.lower() == answer.textData.lower():
                answer.score = self.value
                answer.markCompleted()
        answer.markGraded()
        return