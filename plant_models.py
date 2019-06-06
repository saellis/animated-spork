from google.appengine.ext import ndb

class Plant(ndb.Model):
      name = ndb.StringProperty(required=True)
      color = ndb.StringProperty(required=True)
      description = ndb.StringProperty(required=True)
      url = ndb.StringProperty(required=True)