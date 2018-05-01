#!/usr/bin/env python
import os
import sys

filename = "requirements.txt"
if sys.argv[1]:
    filename = sys.argv[1]

f = open(filename).readlines()

for x in f:
        os.system("pip install "+x)

