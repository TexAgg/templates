import sys
import os

def create_project(project, folder):
#{
	# Get name for this path.
	# http://stackoverflow.com/a/5137509/5415895
	this_path = os.path.dirname(os.path.realpath(__file__))

	# Check if the folder exists, and create it if necessary.
	# http://stackoverflow.com/a/273227/5415895
	if not os.path.exists(folder):
		os.makedirs(folder)
	if not os.path.exists(folder + "/scripts"):
		os.mkdir(folder + "/scripts")

	os.system("m4 " + this_path + "/tsconfig.json.m4 > " + folder + "/tsconfig.json")
	os.system("m4 " + this_path + "/main.ts.m4 > " + folder + "/scripts/main.ts")
	os.system("m4 " + this_path + "/build.py.m4 > " + folder + "/build.py")
	os.system("m4 -DPROJECT='" +  project + "' " + this_path + "/README.md.m4 >" + folder + "/README.md")
#}