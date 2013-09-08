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
		rendered = renderer.render('admin/game/list.html', { 'games': self.games() })
		self.response.write(rendered)

	def games(self):
		return GameModel.query().fetch()

class AdminGameEditController(webapp2.RequestHandler):
	# GET /admin/game/edit
	def get(self):
		game = self.get_game()
		rendered = renderer.render('admin/game/edit.html', { 'game': game })
		self.response.write(rendered)

	# POST /admin/game/edit
	def post(self):
		self.update_game();
		self.get()

	def get_game(self):
		id = int(self.request.get('id'))
		return MOCK_GAMES[id] if id < len(MOCK_GAMES) else None

	def update_game(self):
		game = self.get_game()
		if game:
			game['name'] = self.request.get('name')
			game['description'] = self.request.get('description')
		else:
			game = {
				'id': self.request.get('id'),
				'name': self.request.get('name'),
				'description': self.request.get('description')
			}
		MOCK_GAMES[int(game['id'])] = game

class AdminPuzzleEditController(webapp2.RequestHandler):
	# GET /admin/puzzle/edit
	def get(self):
		game = self.get_game()
		puzzle_id = int(self.request.get('puzzle'))
		puzzle = game['puzzles'][puzzle_id] if puzzle_id < len(game['puzzles']) else { 'id': puzzle_id }
		rendered = renderer.render('admin/puzzle/edit.html', { 
			'puzzle': puzzle,
			'puzzle_id': puzzle_id,
			'game': game['id']
		})
		self.response.write(rendered)

	def post(self):
		self.update_puzzle()
		self.get()

	def get_game(self):
		id = int(self.request.get('game'))

		#return MOCK_GAMES[id] if id < len(MOCK_GAMES) else None

	def update_puzzle(self):
		game = self.get_game()
		puzzle_id = int(self.request.get('puzzle'))
		puzzle = game['puzzles'][puzzle_id] if puzzle_id < len(game['puzzles']) else {}
		puzzle['name'] = self.request.get('name')
		puzzle['description'] = self.request.get('description')
		puzzle['answer'] = self.request.get('answer')
		if puzzle_id < len(game['puzzles']):
			game['puzzles'][puzzle_id] = puzzle
		else:
			game['puzzles'].append(puzzle)

class AdminGameNewController(webapp2.RequestHandler):
	# GET /admin/game/new
	def get(self):
		rendered = renderer.render('admin/game/new.html', {})
		self.response.write(rendered)

	# POST /admin/game/new
	def post(self):
		# TODO: Construct Game object and pass in here
		id = self.add_game(None)
		self.redirect("/admin/game/edit?id=" + str(id))

	def add_game(self, game):
		# TODO: Insert Game object and return id
		return 0
	
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
	('/admin/game/new', AdminGameNewController),
	('/admin/puzzle/edit', AdminPuzzleEditController),
    ('/', IndexController)
], debug=True)