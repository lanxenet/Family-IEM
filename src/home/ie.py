# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''

from datetime import date

from ext import webapp
from model import models

class Submit(webapp.RequestHandler):            
    def post(self):
        detail = models.Detail()
        
        year, month, day = map(int, self.request.get('date').split("/"))
        detail.date = date(year, month, day)
        subjectName = self.request.get('subject')
        subjects = models.Subject.gql("WHERE name = :name AND family IN('default', :family)", 
                                      name=subjectName, 
                                      family=self.family.family_name)
        if not subjects.count():
            subject = models.Subject()
            subject.name = subjectName
            subject.family = self.family.family_name
            subject.put()
            
        detail.subject = subjectName
        ie_type = int(self.request.get('ie_type'))
        detail.ie_type = ie_type
        amount = float(self.request.get('amount').replace(',',''))
        detail.amount = amount if ie_type % 2 == 1 else amount * -1
        detail.family = self.family.family_name
        detail.creator = self.user
        detail.stakeholder = self.request.get('stakeholder')
        detail.description = self.request.get('description')

        detail.put()
        self.redirect('/')
