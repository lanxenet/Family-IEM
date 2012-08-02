# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

from datetime import date
from google.appengine.api import users

from ext import webapp
from model import models

class Members(webapp.RequestHandler):
    def get_internal(self):
        details = models.Family.gql("WHERE creator = :creator and date >= :begin ORDER BY date DESC",
        creator=users.get_current_user(),
        begin=date(today.year, today.month, 1))
        return 'member.html', {}
    
class Settings(webapp.RequestHandler):
    def __init__(self, request=None, response=None):
        webapp.RequestHandler.__init__(self, request, response)
        
        
    def get_internal(self):
        return 'settings.html', {}
    

app = webapp.WSGIApplication([('/account', Members),
                              ('/account/settings', Settings)],
                              debug=True)
