'''
Created on Sep 7, 2013

@author: Phillip
'''

from Key import Key
from google.appengine.ext import ndb

class TextKeyModel(ndb.Model):
    answers = ndb.StringProperty(repeated=True)
    value = ndb.IntegerProperty()
    first = ndb.IntegerProperty()
    second = ndb.IntegerProperty()
    third = ndb.IntegerProperty()
    id = ndb.StringProperty()
    
class TextKey(Key):
    '''
    classdocs
    '''


    def __init__(self, answers, value):
        '''
        Constructor
        '''
        super(TextKey, self).__init__()
        self.answers = answers
        self.value = value
        
    def gradeAnswer(self, answer):
        try:
            for candidate in self.answers:
                if candidate.lower() == answer.textData.lower():
                    answer.score = self.value + self.getBonus(self.parent.countCorrectSolutions())
                    answer.owner.completedMinigames[answer.id] = answer
                    answer.markCompleted()
        except:
            pass
        answer.markGraded()
    @staticmethod
    def createFromAppEngine(id):
        key_query = TextKeyModel.query(TextKeyModel.id == id)
        key = key_query.fetch(1)[0]
        return TextKey(key.answers, key.value)