from google.appengine.api import users

import webapp2

class MainPage(webapp2.RequestHandler):
	# GET for /
	def get(self):
		# Get the logged in user
		user = users.get_current_user()

		# Check if there is a logged in user
		if user:
			# If logged in, respond saying hello to the user
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write('Herro ' + user.nickname())
		else:
			# Otherwise redirect to the login page
			self.redirect(users.create_login_url(self.request.uri))

# Routes
application = webapp2.WSGIApplication([
	# Map / to the MainPage request handler
	('/', MainPage)
], debug=True)