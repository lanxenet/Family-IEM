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
    status = db.StringProperty(default="0")
    
class Family(db.Model):
    user = db.UserProperty()
    email = db.StringProperty()
    role = db.StringProperty()
    family_name = db.StringProperty()

class Subject(db.Model):
    name = db.StringProperty()
    family = db.StringProperty()