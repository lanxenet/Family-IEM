# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

from ext import webapp
from apps.account import handlers

app = webapp.WSGIApplication([('/account/membership', handlers.Membership),
                              ('/account/addmember', handlers.AddMember),
                              ('/account/settings', handlers.Settings),
                              ('/account/', handlers.Membership)],
                              debug=True)
