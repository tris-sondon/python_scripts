#!/usr/bin/env python

"""
Script to rename files by replacing spaces with underscores,
numbers to padded 2 zeros format, remove first two hiphens.

Example:

    This script will rename files that are in the format:

       1 - 1 - Course Introduction (14_11).mp4
       10 - 2 - Using Patterns to Extract Relations (6_17).mp4
       11 - 1 - Week 3 - Part I.mp4
       2 - 2 - Regular Expressions in Practical NLP (6_04).mp4

    to the following format:

       01_01_Course_Introduction_(14_11).mp4
       02_02_Regular_Expressions_in_Practical_NLP_(6_04).mp4
       10_02_Using_Patterns_to_Extract_Relations_(6_17).mp4
       11_01_Week_3-Part_I.mp4

Use:

    - You need to be in the directory where your files are
    - To filter which files to rename, modify the argument of the 
      os.listdir() call.
    - Can be easily integrated into a shell script to process 
      multiple directories.
"""

__author__ = "Tristana Sondon"
__copyright__ = "Copyright 2014, Tristana Sondon"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "tristana.sondon@gmail.com"


import os

for filename in os.listdir("."):
    if filename.find(" ") > 0:
        fsp = filename.split()
        new_filename = ("".join(fsp[0].zfill(2) + "_" + fsp[2].zfill(2) + "_" +
                        "_".join(fsp[4:]))).replace("_-_","-")

        try:
            os.rename(filename, new_filename)
        except:
            print "Exception: ", str(sys.exc_info())


