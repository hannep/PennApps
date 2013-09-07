'''
Created on Sep 7, 2013

@author: Phillip
'''

from Question import Question
from google.appengine.ext import ndb

class TextQuestionModel(ndb.Model):
    id = ndb.StringProperty()
    string = ndb.StringProperty(indexed=False)


class TextQuestion(Question):
    '''
    classdocs
    '''


    def __init__(self, text = "", parent = None):
        '''
        Constructor
        '''
        self.text = text
        super(TextQuestion, self).__init__(parent)
        
    def getTextRepresentation(self):
        return self.text
    
    @staticmethod
    def createFromAppEngine(id):
        question_query = TextQuestionModel.query(TextQuestionModel.id == id)
        question = question_query.fetch(1)[0]
        return TextQuestion(question.string)