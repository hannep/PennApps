import jinja2
import os

### 
# Template config
###
JINJA_TEMPLATE_DIR = os.path.dirname(__file__) + '/../frontend/templates'
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(JINJA_TEMPLATE_DIR),
    extensions=['jinja2.ext.autoescape'])

###
# Helpers
###
def render(template_name, template_values):
	template = JINJA_ENVIRONMENT.get_template('index.html')
	return template.render(template_values)