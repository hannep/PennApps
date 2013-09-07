'''
Created on Sep 7, 2013

@author: Phillip
'''

from Person import Person
from google.appengine.ext import ndb

class AdminModel(ndb.Model):
    phone = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    name = ndb.StringProperty(indexed=False)

class Admin(Person):
    '''
    classdocs
    '''


    def __init__(self, email, phone, name):
        '''
        Constructor
        '''
        super(Admin,self).__init__(email, phone, name)
        
    @staticmethod
    def createFromAppEngine():
        admin_query = AdminModel.query()
        admin_list = admin_query.fetch();
        admins = list()
        for admin in admin_list:
            admins.append(Admin(admin.email, admin.phone, admin.name))
        return admins
        