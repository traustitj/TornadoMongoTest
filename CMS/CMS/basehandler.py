import tornado
import tornado.web
import random
from tornado.gen import Task
import logging as log


class BasicHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        return self.get_secure_cookie("user")

