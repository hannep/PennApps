import sys
sys.stdout = sys.stderr

import cherrypy
import xml.etree.ElementTree as ET
import sqlite3
import os
import datetime
from jinja2 import FileSystemLoader 
from jinja2 import Environment
path = os.path.abspath(os.path.dirname(__file__))
loader = FileSystemLoader(path) 
env = Environment(loader=loader)

PUNCTUATION = "!@#$%^&*()+{}[]`~\\|'\";:/?.>,<"

class Root(object):

    def getConnection(self): 
        return sqlite3.connect(os.path.join(path, "answers.db"))  
    
    def parse_row(self, row): 
        return {"number": row[0], "answer": row[1], "correct": row[2], "timestamp": row[3]}
        

    def dashboard(self) : 
        template = env.get_template('template.html')
        with self.getConnection() as conn: 
            cursor = conn.cursor() 
            cursor.execute("SELECT * FROM Texts;")
            rows = cursor.fetchall()
            texts = [self.parse_row(row) for row in rows]
        return template.render(texts=texts) 
        #return str(rows)
        
    
    dashboard.exposed = True  
        
    def is_correct(self, body):
        if ' ' not in body:
            return False
        location, answer = [x.strip().strip(PUNCTUATION).lower() for x in body.split(' ', 1)]

        answer = answer.strip().lower()
        with sqlite3.connect(os.path.join(path, "answers.db")) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Text FROM answers WHERE LocationTag = ?", [location.lower()])
            correct_answers = set([row[0].lower() for row in cursor.fetchall()])
        return answer in correct_answers

    def index(self, **args):
        number = args["From"]
        body = args["Body"]
        correct = self.is_correct(body)
        time = datetime.datetime.utcnow()
        with sqlite3.connect(os.path.join(path, "answers.db")) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Texts (PhoneNumber, Body, Correct, Time) VALUES (?,?,?,?)",
                [number, body, correct, time]
            )
        cherrypy.response.headers['Content-Type'] = 'text/xml'
        response = ET.Element("Response")
        sms = ET.Element("Sms")
        sms.text = "CORRECT!" if self.is_correct(args["Body"]) else "WRONG!"
        response.append(sms)
        return ET.tostring(response)
    index.exposed = True

#cherrypy.quickstart(Root())
#application = cherrypy.Application(Root(), script_name=None, config=None)
