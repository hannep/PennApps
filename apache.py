import app 
import cherrypy
cherrypy.config.update({
  'environment': 'embedded',
  'request.show_tracebacks': True,
})
application = cherrypy.Application(app.Root(), script_name=None, config=None)

