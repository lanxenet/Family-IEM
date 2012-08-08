# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

from datetime import date
from ext import webapp
from model import models

class About(webapp.RequestHandler):
    def get_with_default_template(self):
        return {}
    
class Home(webapp.RequestHandler):
    def __init__(self, request=None, response=None):
        webapp.RequestHandler.__init__(self, request, response)
        self.type_dict = {}
        self.subjects = []
        import settings
        for key, value in settings.IE_TYPE:
            self.type_dict[value] = key
        if self.user:
            subjects = models.Subject.gql("WHERE family IN('default', :family)", 
                                      family=self.family.family_name)
            for subject in subjects:
                self.subjects.append(subject.name)
        
    def get_handler(self):
        today = date.today()
        details = models.Detail.gql("WHERE family = :family and date >= :begin ORDER BY date DESC",
           family=self.family.family_name,
           begin=date(today.year, today.month, 1))

        import settings
        template_values = {
            'type_dict': self.type_dict,
            'details': details if details.count() > 0 else None,
            'ie_type': settings.IE_TYPE,
            'subjects': self.subjects,
            }
        
        return  template_values, 'index.html'

from home import ie
app = webapp.WSGIApplication([('/', Home),
                              ('/about', About),
                              ('/submit', ie.Submit)],
                              debug=True)
