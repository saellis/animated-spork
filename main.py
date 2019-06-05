#main.py
# the import section
import webapp2
import os
import jinja2

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        index_template = the_jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render()) #the response

class ResultPage(webapp2.RequestHandler):
    # def get(self): #for a get request
    #     breakfast_template = the_jinja_env.get_template('templates/result.html')
    #     self.response.headers['Content-Type'] = 'text/html'
    #     self.response.write(breakfast_template.render(my_plant="Zanzibar Gem")) #the response

    def post(self):
        breakfast_template = the_jinja_env.get_template('templates/result.html')
        user_plant = self.request.get("userplant")
        self.response.write(breakfast_template.render(my_plant=user_plant)) #the response

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/result', ResultPage),
], debug=True)