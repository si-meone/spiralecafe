import os
from google.appengine.ext.webapp import template


from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db


class Greeting(db.Model): 
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
           'greetings': greetings,
           'url': url,
           'url_linktext': url_linktext,
      }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class MenuPage(webapp.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
           'greetings': greetings,
           'url': url,
           'url_linktext': url_linktext,
      }

        path = os.path.join(os.path.dirname(__file__), 'menu.html')
        self.response.out.write(template.render(path, template_values))

class ContactsPage(webapp.RequestHandler):        
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
           'greetings': greetings,
           'url': url,
           'url_linktext': url_linktext,
      }

        path = os.path.join(os.path.dirname(__file__), 'contacts.html')
        self.response.out.write(template.render(path, template_values))
        

class Guestbook(webapp.RequestHandler):
    def post(self):
        greeting = Greeting()

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()
        sendMail(greeting.content)
        self.redirect('/contacts')

application = webapp.WSGIApplication(
                [('/', MainPage),
                ('/menu', MenuPage),
                ('/contacts', ContactsPage),
                ('/sign', Guestbook)],
                debug=True)

def sendMail(greeting):
    mail.send_mail(sender="administrator@spirale.co.uk",
    to="Simon Nasrallah <simon.nasrallah@googlemail.com>",
    subject="Comment Received",
    body="You received the following comment:\n %s " % greeting)
     
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
