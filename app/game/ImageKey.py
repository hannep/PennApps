'''
Created on Oct 20, 2013

@author: Phillip
'''
from Key import Key

class ImageKey(Key):
    '''
    classdocs
    '''

    def __init__(self, value):
        '''
        Constructor
        '''
        super(ImageKey, self).__init__()
        self.value = value
        
    def gradeAnswer(self, answer):
        game = self.parent.parent
        game.addHandGradedAnswer(answer)
