import os

ROOT_PATH = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH , "templates/shared"),
    os.path.join(ROOT_PATH , "templates/home"),
)

IE_TYPE = [
    ("Expenses", 0),
    ("Income", 1),
    ("Lend", 2),
    ("Refund", 3),
    ("Other", 4),
]

SUBJECTS = [
    ("meals", 0),
    ("transportation", 1),
    ("Other", 4),
]

Debug = True
