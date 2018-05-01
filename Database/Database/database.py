from motor import MotorClient
import motor
import tornado
import tornado.gen
from tornado.gen import Task
from PIL import Image
from PIL import ImageOps
import StringIO
from bson import ObjectId
from datetime import datetime, timedelta
import re
import uuid
import logging as log
from Utils import *

sizes = {"thumb": (100, 100), }


class ConnectDB(object):
    def connect(self, hosturl, database):
        mongo_client = MotorClient(hosturl)
        self.mongo = mongo_client[database]
        log.info("db setup : %s", self.mongo)

