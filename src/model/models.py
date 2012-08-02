from google.appengine.ext import db

class Detail(db.Model):
    """docstring for Detail"db.Model"""
    date = db.DateProperty(auto_now_add=True)
    amount = db.FloatProperty()
    ie_type = db.IntegerProperty()
    subject = db.IntegerProperty()
    creator = db.UserProperty()
    stakeholder = db.StringProperty()
    description = db.StringProperty()
    
class Family(db.Model):
    user = db.UserProperty()
    family_name = db.StringListProperty()