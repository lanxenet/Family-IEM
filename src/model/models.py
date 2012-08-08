from google.appengine.ext import db

class Detail(db.Model):
    """docstring for Detail"db.Model"""
    date = db.DateProperty(auto_now_add=True)
    amount = db.FloatProperty()
    ie_type = db.IntegerProperty()
    subject = db.StringProperty()
    family = db.StringProperty()
    creator = db.UserProperty()
    stakeholder = db.StringProperty()
    description = db.StringProperty()
    
class Family(db.Model):
    user = db.UserProperty()
    role = db.StringProperty()
    family_name = db.StringProperty()

class Subject(db.Model):
    name = db.StringProperty()
    family = db.StringProperty()