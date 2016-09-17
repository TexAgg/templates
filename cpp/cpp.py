import sys
import os

folder = sys.argv[1]
project = sys.argv[2]

# Get name for this path.
# http://stackoverflow.com/a/5137509/5415895
this_path = os.path.dirname(os.path.realpath(__file__))

# Check if the folder exists, and create it if necessary.
# http://stackoverflow.com/a/273227/5415895
if not os.path.exists(folder):
	os.makedirs(folder)

os.system("m4 -DPROJECT='" + project + "' " + this_path + "/CMakeLists.txt.m4 > " + folder + "/CMakeLists.txt")
os.system("m4 " + this_path + "/main.cpp.m4 > " + folder + "/main.cpp")