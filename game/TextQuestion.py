'''
Created on Sep 7, 2013

@author: Phillip
'''

from game.Question import Question

class TextQuestion(Question):
    '''
    classdocs
    '''


    def __init__(self, text = "", parent = None):
        '''
        Constructor
        '''
        self.text = text
        super(TextQuestion, self).__init__(parent)
        
    def getTextRepresentation(self):
        return self.text