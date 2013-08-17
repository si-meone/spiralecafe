import  webapp2


class Calculator(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        num1 = int(self.request.get("num1")) or 0
        num2 = int(self.request.get("num2")) or 0

        result = self.add(num1, num2)
        self.response.write('Result of Adding %s and %s is  %s' %(num1, num2, result))

    def add(self, num1 , num2):
        return num1 + num2


application = webapp2.WSGIApplication([
    ('/scripts/calc', Calculator)], debug=True)
