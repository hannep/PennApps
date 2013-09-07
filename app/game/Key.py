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

    def __init__(self, value = 0, firstPlace = 0, secondPlace = 0, thirdPlace = 0,isHandGraded = False):
        '''
        Constructor
        '''
        self.parent = None
        self.value = value
        self.first = 0
        self.second = 0
        self.third = 0
        self.isHandGraded = isHandGraded
        
    def getBonus(self, pos):
        if pos == 0:
            return self.first
        elif pos == 1:
            return self.second
        elif pos == 2:
            return self.third
        else:
            return 0;
        
    @abstractmethod
    def gradeAnswer(self, answer):
        pass