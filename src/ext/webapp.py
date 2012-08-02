# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

import webapp2

from model import models
from ext import template
from google.appengine.api import users

class RequestHandler(webapp2.RequestHandler):
    """Base HTTP request handler.

    extension the ``webapp2.RequestHandler`` class.
    """
    
    def __init__(self, request=None, response=None):
        webapp2.RequestHandler.__init__(self, request, response)
        self.user = users.get_current_user()
        self.url = 'Login'
        self.url_linktext = None
        if self.user:
            self.family = models.Family.gql("WHERE user = :user", self.user)
            if not self.family:
                account = models.Family()
                account.user = self.user
                account.family_name = self.user.nickname()
                account.put()
                
    def get(self):
        self.user = users.get_current_user()
        if self.user:
            self.url = users.create_logout_url(self.request.uri)
            self.url_linktext = 'Logout'
        else:
#            self.url = users.create_login_url(self.request.uri)
#            self.url_linktext = 'Login'
            self.redirect(self.url)
            
        template_name, template_dict = self.get_internal()
        
        template_dict['user'] = self.user
        template_dict['url'] = self.url
        template_dict['url_linktext'] = self.url_linktext
        
        return self.response.out.write(template.render(template_name, template_dict))  

    def get_internal(self):
        pass
        
    def port(self):
        self.user = users.get_current_user()
        if self.user:
            self.url = users.create_logout_url(self.request.uri)
            self.url_linktext = 'Logout'
        else:
            self.url = users.create_login_url(self.request.uri)
            self.url_linktext = 'Login'
            self.redirect(self.url)
        
        template_name, template_dict = self.post_internal()        
        return self.response.out.write(template.render(template_name, template_dict)) 
    
    def post_internal(self):
        pass  
    
class WSGIApplication(webapp2.WSGIApplication):
    """A EXT WSGI-compliant application."""
        
