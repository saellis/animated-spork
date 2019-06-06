#main.py
# the import section
import webapp2
import os
import jinja2

from seed import seed_db

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

color_relationships = {
    'Black': ['Grey', 'White'],
    'Green': ['Red', 'Purple'], 
    'Grey': ['Black', 'White'],
    'Purple': ['Yellow'],
    'Red': ['Green'],
    'Yellow': ['Purple'],
    'White': ['Black', 'Grey']
}

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        index_template = the_jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render()) #the response

class SeedPage(webapp2.RequestHandler):
    def get(self): #for a get request
        seed_db()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("<h1>Database seeded! .. Get it?</h1>") #the response

class ResultPage(webapp2.RequestHandler):
    def post(self):
        results_template = the_jinja_env.get_template('templates/result.html')
        space_color = self.request.get("space_color")

        plant_colors = color_relationships[space_color]
        plant_colors_string = plant_colors[0]
        for color in plant_colors[1:]:
            plant_colors_string += " and " + color

        plant_url = "https://cdn.shopify.com/s/files/1/0150/6262/products/the-sill_snake-plant-slaurentii_terracotta_4_800x.jpg?v=1537308389"

        self.response.write(results_template.render(my_plant=plant_colors_string, image_link=plant_url)) #the response

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/result', ResultPage),
    ('/seed', SeedPage),
], debug=True)
