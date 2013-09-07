import cgi
import urllib
import webapp2

MAIN_PAGE_HTML = """\
<html>
	<body>
		<form method="post">
			<input type="text" name="query">
			<input type="submit" value="Submit">
		</form>
	</body>
</html>
"""

REDDIT_SEARCH_URL = 'http://www.reddit.com/search.json?q='

class MainPage(webapp2.RequestHandler):
	# GET for /
	def get(self):
		self.response.write(MAIN_PAGE_HTML)

	# POST for /
	def post(self):
		url = REDDIT_SEARCH_URL + cgi.escape(self.request.get('query'))
		result = urllib.urlopen(url)
		self.response.headers['Content-Type'] = 'application/json'
		self.response.write(result.read())


# Routes
application = webapp2.WSGIApplication([
	# Map / to the MainPage request handler
	('/', MainPage),
], debug=True)