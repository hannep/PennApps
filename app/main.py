###
# Library imports
###
import webapp2

###
# App imports
###
from utils import renderer
from game import *

###
# Temporary constants for interface dev
###
MOCK_GAMES = [{
	'id': 0,
	'name': 'Super awesome game',
	'description': 'This game is so awesome omg omg.',
	'participants': [
		{ 'name': 'Mark Fielbig' },
		{ 'name': 'Phil Huff' }
	],
	'puzzles': [{ 
		'name': 'mindfuck' ,
		'description': 'omgwtfsolvethisshit',
		'answer': '42'
	}]
}, {
	'id': 1,
	'name': 'Not so awesome game',
	'description': 'Weeeeeeeeak.',
	'participants': [
		{ 'name': 'Mark Fielbig' },
		{ 'name': 'Phil Huff' }
	],
	'puzzles': [{ 
		'name': 'lolwhat?' ,
		'description': 'easssssy',
		'answer': ':)'
	}]
}]

game = Game(name='Game', description='Default game')

###
# Controllers
###
class IndexController(webapp2.RequestHandler):
	# GET /
    def get(self):
    	rendered = renderer.render('index.html', { 'message': 'heyo' })
        self.response.write(rendered)

class AdminGameController(webapp2.RequestHandler):
	# GET /admin/game
	def get(self):
		rendered = renderer.render('admin/game/list.html', { 'game': game })
		self.response.write(rendered)

class AdminGameEditController(webapp2.RequestHandler):
	# GET /admin/game/edit
	def get(self):
		rendered = renderer.render('admin/game/edit.html', { 'game': game })
		self.response.write(rendered)

	# POST /admin/game/edit
	def post(self):
		self.update_game();
		self.get()

	def update_game(self):
		game.name = self.request.get('name')
		game.description = self.request.get('description')

class AdminPuzzleEditController(webapp2.RequestHandler):
	# GET /admin/puzzle/edit
	def get(self):
		puzzle = game.minigames.get(self.request.get('name'))
		rendered = renderer.render('admin/puzzle/edit.html', { 'puzzle': puzzle })
		self.response.write(rendered)

	def post(self):
		puzzle = game.minigames.get(self.request.get('name'))
		if not puzzle:
			puzzle = Minigame(
				name=self.request.get('name'), 
				answer=self.request.get('answer'), 
				question=self.request.get('question'))
			game.minigames[puzzle.name] = puzzle
		else:
			puzzle.name = self.request.get('name')
			puzzle.answer = self.request.get('answer')
			puzzle.question = self.request.get('question')
		self.get()
	
class PuzzleAnswerController(webapp2.RequestHandler):
	def post(self):
		type = self.request.get("type").lower()
		data = None
		if type == "text":
			data = self.request.get("text")
		elif type == "image":
			data = self.request.get("url")
		elif type == "location":
			lat = self.request.get("latitude")
			long = self.request.get("longitude")
			data = geopy.Point(latitude = lat, longitude = long)
		minigame = self.request.get("puzzleId")
		number = self.request.get("number")
		#get user from number
		user_query = UserModel.query(UserModel.phone == number)
		users = user_query.fetch(1)
		user = None
		if len(users) > 0:
			user = users[0]
		else:
			return
		answer = Answer(user, minigame, data)
		#get singleton Game object
		
###
# Routes
###
application = webapp2.WSGIApplication([
	('/admin/game', AdminGameController),
	('/admin/game/edit', AdminGameEditController),
	('/admin/puzzle/edit', AdminPuzzleEditController),
    ('/', IndexController)
], debug=True)