import os

Debug = True

ROOT_PATH = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH , "templates/shared"),
    os.path.join(ROOT_PATH , "templates/home"),
    os.path.join(ROOT_PATH , "templates/account"),
)

IE_TYPE = [
    ("Expenses", 0),
    ("Income", 1),
    ("Lend", 2),
    ("Refund", 3),
]

SUBJECTS = [
    "meals",
    "transportation",
]


ADD_MEMBER_MAIL_SUBJECT_FORMAT = "I've added you to %s  on Family-IEM"

ADD_MEMBER_MAIL_BODY_FORMAT = """
        Hi %s, you have been invited by %s to the IEM account: %s
        
        Please let us know if you have any questions.
        
        The family-apps.me Team"""

SUPPORT_MAIL = "Family-apps Support <support@family-apps.me>"
     

