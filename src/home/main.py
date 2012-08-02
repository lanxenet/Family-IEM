# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

from datetime import date
from google.appengine.api import users

from ext import webapp
from model import models

class About(webapp.RequestHandler):
    def get_internal(self):
        return 'about.html', {}
    
class Home(webapp.RequestHandler):
    def __init__(self, request=None, response=None):
        webapp.RequestHandler.__init__(self, request, response)
        self.type_dict = {}
        self.subject_dict = {}
        import settings
        for key, value in settings.IE_TYPE:
            self.type_dict[value] = key
        
        for key, value in settings.SUBJECTS:
            self.subject_dict[value] = key
        
        
    def get_internal(self):
        today = date.today()
        details = models.Detail.gql("WHERE creator = :creator and date >= :begin ORDER BY date DESC",
           creator=users.get_current_user(),
           begin=date(today.year, today.month, 1))

        import settings
        template_values = {
            'type_dict': self.type_dict,
            'subject_dict': self.subject_dict,
            'details': details if details.count() > 0 else None,
            'ie_type': settings.IE_TYPE,
            'subjects': settings.SUBJECTS,
            }
        
        return 'index.html', template_values

from home import ie
app = webapp.WSGIApplication([('/', Home),
                              ('/about', About),
                              ('/submit', ie.Submit)],
                              debug=True)
