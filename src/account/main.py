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
        members = models.Family.gql("WHERE family_name = :family", family = self.family)
        values = {
            'members': members}
        return 'member.html', values

class Memberships(webapp.RequestHandler):
    def get_internal(self):
        members = models.Family.gql("WHERE family_name = :family", family = self.family)
        values = {
            'members': members}
        return 'member.html', values
    
class Settings(webapp.RequestHandler):
    def __init__(self, request=None, response=None):
        webapp.RequestHandler.__init__(self, request, response)
        
        
    def get_internal(self):
        return 'settings.html', {}
    

app = webapp.WSGIApplication([('/account', Members),
                              ('memberships', Memberships),
                              ('/account/settings', Settings)],
                              debug=True)
