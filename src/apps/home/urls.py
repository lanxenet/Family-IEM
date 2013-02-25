# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

from ext import webapp
from apps.home import handlers

app = webapp.WSGIApplication([('/', handlers.Index),
                              ('/about', handlers.About),
                              ('/submit', handlers.Submit)],
                              debug=True)
