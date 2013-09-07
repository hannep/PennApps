from google.appengine.api import users

import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write('Herro ' + user.nickname())
		else:
			self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
	('/', MainPage)
], debug=True)