###
# Library imports
###
import webapp2

###
# App imports
###
from utils import renderer

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
		return MOCK_GAMES

class AdminGameEditController(webapp2.RequestHandler):
	# GET /admin/game/edit
	def get(self):
		game = self.game_with_id(int(self.request.get('id')))
		rendered = renderer.render('admin/game/edit.html', { 'game': game })
		self.response.write(rendered)

	def game_with_id(self, id):
		return MOCK_GAMES[id]

class AdminPuzzleEditController(webapp2.RequestHandler):
	# GET /admin/puzzle/edit
	def get(self):
		game = self.game_with_id(int(self.request.get('game')))
		puzzle = game['puzzles'][int(self.request.get('puzzle'))]
		rendered = renderer.render('admin/puzzle/edit.html', { 'puzzle': puzzle })
		self.response.write(rendered)

	def game_with_id(self, id):
		return MOCK_GAMES[id]

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