import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Bye, World!')


application = webapp2.WSGIApplication([('/scripts/bye', MainPage)], debug=True)
