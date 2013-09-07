'''
Created on Sep 7, 2013

@author: Phillip
'''
from abc import ABCMeta, abstractmethod

class Key(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta

    def __init__(self, isHandGraded = False):
        '''
        Constructor
        '''
        self.parent = None
        self.isHandGraded = isHandGraded
        
    @abstractmethod
    def gradeAnswer(self, answer):
        pass
        