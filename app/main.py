###
# Library imports
###
import webapp2

###
# App imports
###
from utils import renderer

###
# Controllers
###
class IndexController(webapp2.RequestHandler):
	# GET /
    def get(self):
    	rendered = renderer.render('index.html', { 'message': 'heyo' })
        self.response.write(rendered)

###
# Routes
###
application = webapp2.WSGIApplication([
    ('/', IndexController)
], debug=True)