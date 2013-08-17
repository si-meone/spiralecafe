import  webapp2


class HelloPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')


class HiPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hi, World!')


application = webapp2.WSGIApplication([
    ('/scripts/hello', HelloPage),
    ('/scripts/hi', HiPage)], debug=True)
