#!/usr/bin/env python

"""
Script to rename files by replacing spaces with underscores.
"""

__author__ = "Tristana Sondon"
__copyright__ = "Copyright 2014, Tristana Sondon"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "tristana.sondon@gmail.com"


import os

for filename in os.listdir("."):
    if filename.find(" ") > 0:
        new_filename = filename.replace(" ", "_")

        try:
            os.rename(filename, new_filename)
        except:
            print "Exception: ", str(sys.exc_info())


