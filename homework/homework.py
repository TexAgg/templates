#!/usr/bin/env python

import sys
import os

assignment = sys.argv[1]
folder = sys.argv[2]

# Check if the folder exists, and create it if necessary.
# http://stackoverflow.com/a/273227/5415895
if not os.path.exists(folder):
	os.makedirs(folder)

os.system("m4 -DASSIGNMENT='" +  assignment + "' main.m4 >" + folder + "/main.tex")
os.system("m4 Makefile.m4 > " + folder + "/Makefile")