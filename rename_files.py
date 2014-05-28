#!/usr/bin/env python

import os

for filename in os.listdir("."): 
    if filename.find(" ") > 0: 
        fsp = filename.split()
        new_filename = (''.join(fsp[0].zfill(2) + "_" + fsp[2].zfill(2) + "_" +  
                        "_".join(fsp[4:]))).replace("_-_","-")
        os.rename(filename,new_filename) 

