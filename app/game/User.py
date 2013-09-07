'''
Created on Sep 7, 2013

@author: Phillip
'''
import Person

class User(Person.Person):
    '''
    classdocs
    '''


    def __init__(self, email, phone, name):
        '''
        Constructor
        '''
        super(User,self).__init__(email, phone, name)
        self.completedMinigames = dict()