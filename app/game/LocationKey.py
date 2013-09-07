'''
Created on Sep 7, 2013

@author: Phillip
'''
#import geopy.distance
from Key import Key
from google.appengine.ext import ndb

class LocationKeyModel(ndb.Model):
    latitude = ndb.FloatProperty()
    longitude = ndb.FloatProperty()
    distance = ndb.FloatProperty()
    value = ndb.IntegerProperty()
    first = ndb.IntegerProperty()
    second = ndb.IntegerProperty()
    third = ndb.IntegerProperty()
    id = ndb.StringProperty()

class LocationKey(Key):
    '''
    classdocs
    '''

    def __init__(self, latitude, longitude, distance, value):
        '''
        Constructor
        '''
        super(LocationKey, self).__init__()
        self.value = value
        #self.point = geopy.Point(latitude=latitude, longitude=longitude)
        self.distance = distance
        
    def gradeAnswer(self, answer):
        pass
        # try:
        #     dist = geopy.distance.distance(self.point, answer.data).m
        #     if dist < self.distance:
        #         answer.score = self.value + self.getBonus(self.parent.countCorrectSolutions())
        #         answer.markCompleted()
        # except:
        #     pass
        # answer.markGraded()
        
    @staticmethod
    def createFromAppEngine(self, id):
        key_query = LocationKeyModel.query(LocationKeyModel.id == id)
        key = key_query.fetch(1)[0]
        return LocationKey(key.latitude, key.longitude, key.distance)