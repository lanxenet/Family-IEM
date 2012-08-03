# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

from datetime import date
from google.appengine.api import users

from ext import webapp
from model import models

class Submit(webapp.RequestHandler):            
    def post(self):
        detail = models.Detail()
        
        year, month, day = map(int, self.request.get('date').split("/"))
        detail.date = date(year, month, day)
        detail.subject = int(self.request.get('subject'))
        ie_type = int(self.request.get('ie_type'))
        detail.ie_type = ie_type
        amount = float(self.request.get('amount').replace(',',''))
        detail.amount = amount if ie_type % 2 == 1 else amount * -1
        detail.creator = users.get_current_user()
        detail.stakeholder = self.request.get('stakeholder')
        detail.description = self.request.get('description')

        detail.put()
        self.redirect('/')
