'''
Created on Sep 7, 2013

@author: Phillip
'''

from Question import Question
from google.appengine.ext import ndb

class ImageQuestionModel(ndb.Model):
    id = ndb.StringProperty()
    url = ndb.StringProperty(indexed=False)
    
class ImageQuestion(Question):
    '''
    classdocs
    '''


    def __init__(self, url, parent = None):
        '''
        Constructor
        '''
        super(ImageQuestion, self).__init__(parent)
        self.url = url
        
    def getTextRepresentation(self):
        return self.url
    
    @staticmethod
    def createFromAppEngine(self, id):
        question_query = ImageQuestionModel.query(ImageQuestionModel.id == id)
        question = question_query.fetch(1)[0]
        return ImageQuestion(question.url)