import jinja2
import os
import webapp2

### 
# Template config
###
JINJA_TEMPLATE_DIR = os.path.dirname(__file__) + '/frontend/templates'
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(JINJA_TEMPLATE_DIR),
    extensions=['jinja2.ext.autoescape'])

###
# Controllers
###
class IndexController(webapp2.RequestHandler):
	# GET /
    def get(self):
    	# Make a map of values to pass into the template
        template_values = { 'message': 'heyo' }
        # Get the template object
        template = JINJA_ENVIRONMENT.get_template('index.html')
        # Render the template
        rendered = template.render(template_values)
        # Return the rendered template
        self.response.write(rendered)

###
# Routes
###
application = webapp2.WSGIApplication([
    ('/', IndexController)
], debug=True)