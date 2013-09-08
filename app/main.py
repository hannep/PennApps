###
# Library imports
###
import webapp2
import urllib

###
# App imports
###
from utils import renderer
from game import *

game = Game(name='Stony Brook Puzzle Hunt 2013', description='Explore the campus and solve puzzles in this semesters exciting puzzle hunt! Prizes will be provided to the top 3 teams.')
game.minigames["The Secret Letter"] = Minigame("The Secret Letter", "I USED TO THINK I WAS INDECISIVE, BUT NOW I'M NOT SO SURE.", TextQuestion("What do I say? Q BAWK HI HZQUF Q XVA QUKWTQAQDW, GBH UIX Q'C UIH AI ABEW."))
game.minigames["The Forrester's Riddle"] = Minigame("The Forrester's Riddle", "a splinter", TextQuestion("I went into the woods and got it. I sat down to seek it. I brought it home with me because I couldn't find it. What is it?"))
messages = []

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
				question=TextQuestion(self.request.get('question')))
			game.minigames[puzzle.name] = puzzle
		else:
			puzzle.name = self.request.get('name')
			puzzle.answer = self.request.get('answer')
			puzzle.question = self.request.get('question')
		self.get()

class AdminNotificationController(webapp2.RequestHandler):
	def get(self):
		rendered = renderer.render('admin/notification/broadcast.html', { 'messages': messages })
		return self.response.write(rendered)

	def post(self):
		game.notifyUsers(self.request.get('message'))
		self.get()

class RegisterTeamController(webapp2.RequestHandler):
	def get(self):
		rendered = renderer.render('client/registerteam.html', {})
		self.response.write(rendered)

	def post(self):
		country_code = self.request.get('countrycode')
		mobile_number = self.request.get('cellNum')
		phone_number = country_code + mobile_number
		name = self.request.get('teamName')
		user = User(phone_number, name)
		append_user = True
		for usr in game.users:
			if usr.phone == user.phone:
				append_user = False
				break
		if append_user:
			game.users.append(user)
		self.response.set_status(303)
		self.response.headers['Location'] = '/puzzles?' + urllib.urlencode({"number" : phone_number})
		self.response.write('')

class HelpController(webapp2.RequestHandler):
	def get(self):
		rendered = renderer.render('client/gethelp.html', {})
		self.response.write(rendered)

	def post(self):
		subject = self.request.get('subject')
		message = self.request.get('message')
		messages.append({
			'subject': subject,
			'message': message
		})
		self.get()
	
class LeaderboardController(webapp2.RequestHandler):
	def get(self):
		sorted_users = game.sortUsersByScore()
		rendered = renderer.render('client/playerleaderboard.html', {
			'users': sorted_users
		})
		self.response.write(rendered)

class PuzzleSelectionController(webapp2.RequestHandler):
	def get(self):
		rendered = renderer.render('client/playergamehome.html', { 
			'game': game,
			'number': self.request.get('number')
		})
		self.response.write(rendered)
		
	def post(self):
		self.redirect('/challenge')
		
class PuzzleAnswerController(webapp2.RequestHandler):
	def get(self, message=''):
		puzzle = game.minigames[self.request.get('puzzleId')]
		number = self.request.get('number')
		rendered = renderer.render('client/challenge.html', { 
			'challenge': puzzle,
			'number': number,
			'message': message
		})
		self.response.write(rendered)
		
	def post(self):
		type = self.request.get("type").lower()
		data = None
		if type == "text":
			data = self.request.get("message")
		elif type == "image":
			data = self.request.get("url")
		elif type == "location":
			lat = self.request.get("latitude")
			long = self.request.get("longitude")
			data = geopy.Point(latitude = lat, longitude = long)
		minigame = self.request.get("puzzleId")
		number = self.request.get("number")
		user = None
		for usr in game.users:
			if usr.phone == number:
				user = usr
		if user == None:
			self.response.write("Something went wrong.")
		answer = Answer(user, minigame, data)
		resp = game.checkAnswer(minigame, answer)
		self.get('Correct!' if resp else 'Wrong!')

###
# Routes
###
application = webapp2.WSGIApplication([
	('/admin', AdminGameController),
	('/admin/edit', AdminGameEditController),
	('/admin/puzzle/edit', AdminPuzzleEditController),
	('/admin/notify', AdminNotificationController),
	('/challenge', PuzzleAnswerController),
	('/puzzles', PuzzleSelectionController),
	('/help', HelpController),
	('/scores', LeaderboardController),
    ('/', RegisterTeamController)
], debug=True)