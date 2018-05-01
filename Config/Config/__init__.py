import os
import yaml
import logging

class Config(object):
    def __init__(self, mode="development"):
        pwd = os.path.dirname(os.path.realpath(__file__))
        text = open(pwd+"/siteconfig.yaml","r").read()
        c = yaml.load(text)
        logging.info("config mode is : %s", mode)
        self.config = c[mode]
