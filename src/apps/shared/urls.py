# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

from ext import webapp
from apps.shared import handlers

app = webapp.WSGIApplication([('/help', handlers.Help),
                              ('/error', handlers.Error)],
                              debug=True)
