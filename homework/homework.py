import sys
import os

def create_project(assignment, folder):
#{
	# Get name for this path.
	# http://stackoverflow.com/a/5137509/5415895
	this_path = os.path.dirname(os.path.realpath(__file__))

	# Check if the folder exists, and create it if necessary.
	# http://stackoverflow.com/a/273227/5415895
	if not os.path.exists(folder):
		os.makedirs(folder)

	os.system("m4 -DASSIGNMENT='" +  assignment + "' " + this_path + "/main.tex.m4 >" + folder + "/main.tex")
	os.system("m4 " + this_path + "/Makefile.m4 > " + folder + "/Makefile")
	os.system("m4 -DASSIGNMENT='" +  assignment + "' " + this_path + "/README.md.m4 >" + folder + "/README.md")
#}