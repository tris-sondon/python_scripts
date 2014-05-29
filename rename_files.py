#!/usr/bin/env python

###################################################################
# Author: Tristana Sondon
# Date: May 2014
# Licence: MIT
###################################################################

"""
This script will rename files that are in the format:

   1 - 1 - Course Introduction (14_11).mp4
   10 - 1 - What is Relation Extraction_ (9_47).mp4
   10 - 2 - Using Patterns to Extract Relations (6_17).mp4
   2 - 1 - Regular Expressions (11_25).mp4
   2 - 2 - Regular Expressions in Practical NLP (6_04).mp4

to the following format:

"""

import os

for filename in os.listdir("."): 
    if filename.find(" ") > 0: 
        fsp = filename.split()
        new_filename = ("".join(fsp[0].zfill(2) + "_" + fsp[2].zfill(2) + "_" +  
                        "_".join(fsp[4:]))).replace("_-_","-")
	try:
        	os.rename(filename, new_filename)
	except:
		print "Exception: ",str(sys.exc_info())
