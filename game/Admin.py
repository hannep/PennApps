'''
Created on Sep 7, 2013

@author: Phillip
'''

import Person

class Admin(Person.Person):
    '''
    classdocs
    '''


    def __init__(self, email, phone, name):
        '''
        Constructor
        '''
        super(Admin,self).__init__(email, phone, name)