# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

from ext import webapp

class Error(webapp.RequestHandler):
    def get_internal(self):
        return 'error.html', {}
    
class Help(webapp.RequestHandler):
    def get_internal(self):
        return 'about.html', {}

app = webapp.WSGIApplication([('/help', Help),
                              ('/error', Error)],
                              debug=True)
