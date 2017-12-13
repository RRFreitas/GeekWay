import re
from datetime import datetime

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Validator(Singleton):
    def __init__(self):
        super(Validator, self).__init__()

    def validEmail(self, email):
        return re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email) and len(email) < 51

    def validPassword(self, password):
        return len(password) < 21 and len(password) > 2

    def validName(self, name):
        return len(name) > 2 and len(name) < 100

    def validDate(self, date_text):
        args = date_text.split('/')
        try:
            date = datetime(int(args[2]), int(args[1]), int(args[0]))
            return date
        except:
            return False