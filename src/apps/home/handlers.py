__version__ = "1.0"

__all__ = []


from datetime import date
from ext import webapp
from apps.model import models

class About(webapp.RequestHandler):
    def get_with_default_template(self):
        return {}

class Index(webapp.RequestHandler):
    def __init__(self, request=None, response=None):
        webapp.RequestHandler.__init__(self, request, response)
        self.type_dict = {}
        self.subjects = []
        import settings
        for key, value in settings.IE_TYPE:
            self.type_dict[value] = key
        if self.user:
            subjects = models.Subject.gql("WHERE family IN('default', :family)", 
                                      family=self.family.family_name)
            for subject in subjects:
                self.subjects.append(subject.name)
        
    def get_handler(self):
        today = date.today()
        details = models.Detail.gql("WHERE family = :family and date >= :begin ORDER BY date DESC",
           family=self.family.family_name,
           begin=date(today.year, today.month, 1))

        import settings
        template_values = {
            'type_dict': self.type_dict,
            'details': details if details.count() > 0 else None,
            'ie_type': settings.IE_TYPE,
            'subjects': self.subjects,
            }
        
        return  template_values, 'index.html'

class Submit(webapp.RequestHandler):            
    def post(self):
        detail = models.Detail()
        
        day, month, year = map(int, self.request.get('date').split("/"))
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