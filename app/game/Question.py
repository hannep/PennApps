'''
Created on Sep 7, 2013

@author: Phillip
'''
from abc import ABCMeta, abstractmethod

class Question(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta

    def __init__(self, parent):
        '''
        Constructor
        '''
        self.parent = parent
        
    @abstractmethod
    def getTextRepresentation(self):
        pass