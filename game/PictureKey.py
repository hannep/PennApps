'''
Created on Sep 7, 2013

@author: Phillip
'''

from game.Key import Key

class PictureKey(Key):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(PictureKey, self).__init__()
        self.isHandGraded = True