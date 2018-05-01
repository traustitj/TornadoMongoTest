#!/usr/bin/env python
from tornado import template

import os
import os.path
import json
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import redis as Redis
from tornado.gen import Task
from Database import ConnectDB
from Store import StoreDatabase
from Store import CategoriesHandler
from Config import Config
from tornado.options import define, options

define("port", default=8000, help="must use a port number", type=int)
define("debug", default=True, help="debug or not to debug?", type=bool)


class DB(ConnectDB, StoreDatabase):
    def nothing(self):
        print "Version 1.0"

class Application(tornado.web.Application):
    def __init__(self,):
        handlers = [
            (r'/api/categories', CategoriesHandler),
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=options.debug,
            multiple=True,
            cookie_secret="sosueme",
        )
        self.config = None
        if options.debug:
            os.environ["rundev"] = "development"
            self.config = Config(mode="development").config

        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = DB()
        self.db.connect(self.config["database"]["host"],
                        self.config["database"]["database"])
        static_path = settings["static_path"]

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
