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
        self.url = None
        self.url_linktext = 'Login'
        if self.user:
            self.family = models.Family.gql("WHERE user = :user", user=self.user).get()
            if not self.family:
                account = models.Family()
                account.user = self.user
                account.role = "Owner"
                account.family_name = self.user.nickname()
                account.put()
                self.family = account                
                
    def get(self):
        self.user = users.get_current_user()
        if not self.user:
            return self.redirect(users.create_login_url(self.request.uri))
        
        self.url = users.create_logout_url(self.request.uri)
        self.url_linktext = 'Logout'            
        template_dict, template_name = self.get_handler()
        
        template_dict['user'] = self.user
        template_dict['url'] = self.url
        template_dict['url_linktext'] = self.url_linktext
        
        return self.response.out.write(template.render(template_name, template_dict))  

    def get_handler(self):
        template_dict = self.get_with_default_template()
        return template_dict, self.get_default_template_name()
    
    def get_with_default_template(self):
        pass
        
    def port(self):
        self.user = users.get_current_user()
        if not self.user:
            return self.redirect(users.create_login_url(self.request.uri))
        
        self.url = users.create_logout_url(self.request.uri)
        self.url_linktext = 'Logout'           
    
        template_dict, template_name = self.post_handler() 
            
        return self.response.out.write(template.render(template_name, template_dict)) 
    
    def post_handler(self):
        template_dict = self.post_with_default_template()
        return template_dict, self.get_default_template_name()
    
    def post_with_default_template(self):
        pass
    
    def get_default_template_name(self):
        return (self.__class__.__name__ + '.html').lower()
    
class WSGIApplication(webapp2.WSGIApplication):
    """A EXT WSGI-compliant application."""
