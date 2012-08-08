# -*- coding: utf-8 -*-
'''
Created on 2012-7-30

@author: lanxe
'''
import logging
from google.appengine.api import users
from ext import webapp
from model import models

class Membership(webapp.RequestHandler):
    def get_with_default_template(self):
        members = models.Family.gql("WHERE family_name = :family", family=self.family.family_name)
        values = {
            'members': members if members.count() > 0 else None, }
        return  values
 
class AddMember(webapp.RequestHandler):
    def post(self):
        member = self.request.get('member_string')
        members = models.Family.gql("WHERE family_name = :family AND user = :user", family=self.family.family_name, user=users.User(email=member))
        if not members.count():
            family = models.Family()          
            family.user = users.User(email=member)
            family.role = self.request.get('account_role')
            family.family_name = self.family.family_name    
            family.put()
            try:
                self.send_mail(member)
            except Exception, e:
                logging.info(e)
                
        self.redirect('/account/membership')

    def send_mail(self, receiver):
        import settings
        from google.appengine.api import mail
        
        mail.send_mail(sender=settings.SUPPORT_MAIL,
                      to=receiver,
                      subject=(settings.ADD_MEMBER_MAIL_SUBJECT_FORMAT % self.family.family_name),
                      body=(settings.ADD_MEMBER_MAIL_BODY_FORMAT % (receiver, self.family.family_name, self.user.nickname())))

   
class Settings(webapp.RequestHandler):
    def __init__(self, request=None, response=None):
        webapp.RequestHandler.__init__(self, request, response)
        
        
    def get_handler(self):
        return {}, 'settings.html'
    

app = webapp.WSGIApplication([('/account/', Membership),
                              ('/account/membership', Membership),
                              ('/account/addmember', AddMember),
                              ('/account/settings', Settings)],
                              debug=True)
