#!/usr/bin/env python

###################################################################
# Author: Tristana Sondon
# Date: May 2014
# Licence: MIT
###################################################################

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
