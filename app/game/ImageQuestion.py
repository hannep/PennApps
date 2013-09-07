'''
Created on Sep 7, 2013

@author: Phillip
'''

from game.Question import Question

class ImageQuestion(Question):
    '''
    classdocs
    '''


    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(ImageQuestion, self).__init__(parent)
        
    def getTextRepresentation(self):
        return ""