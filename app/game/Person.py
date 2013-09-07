'''
Created on Sep 7, 2013

@author: Phillip
'''
from twilio.rest import TwilioRestClient

class Person(object):
    '''
    classdocs
    '''
    fromNum = "+11234567890"
    account_sid = ""
    auth_token = ""
    
    client = TwilioRestClient(account_sid, auth_token)

    def __init__(self, email, phone, name):
        '''
        Constructor
        '''
        self.email = email
        self.phone = phone
        self.name = name
        
    def sendEmail(self, msg):
        pass
    def sendText(self, msg):
        message = Person.client.sms.messages.create(to=self.phone, from_=Person.fromNum, body=msg)