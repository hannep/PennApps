'''
Created on Sep 7, 2013

@author: Phillip
'''
from Question import Question
from google.appengine.ext import ndb

class ImageQuestionModel(ndb.Model):
    id = ndb.StringProperty()
    string = ndb.StringProperty(indexed=False)
    url = ndb.StringProperty(indexed=False)
    

class CompositeQuestion(Question):
    '''
    classdocs
    '''


    def __init__(self, text, url, parent = None):
        '''
        Constructor
        '''
        super(CompositeQuestion, self).__init__(parent)
        self.url = url
        self.text = text
        
    def getTextRepresentation(self):
        return "text:" + self.text + ";" + "\nimg:" +self.url + ";"
    
    @staticmethod
    def createFromAppEngine(self, id):
        question_query = ImageQuestionModel.query(ImageQuestionModel.id == id)
        question = question_query.fetch(1)[0]
        return CompositeQuestion(question.string, question.url)