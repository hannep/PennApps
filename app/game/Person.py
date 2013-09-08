'''
Created on Sep 7, 2013

@author: Phillip
'''
from twilio.rest import TwilioRestClient

class Person(object):
    '''
    classdocs
    '''
    fromNum = "+16316157486"
    account_sid = "AC87e3e47533f35abf2ee9f1cfe46ba62f"
    auth_token = "1e77d75cccbccbd0467e4a14f36538eb"
    
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
        try:
            message = Person.client.sms.messages.create(to=self.phone, from_=Person.fromNum, body=msg)
        except:
            pass #whoops!
