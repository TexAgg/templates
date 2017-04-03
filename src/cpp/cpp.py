import sys
import os
# http://stackoverflow.com/a/1054281/5415895
from ..render import Renderer

def create_project(project, folder):
#{
	# Get name for this path.
	# http://stackoverflow.com/a/5137509/5415895
	this_path = os.path.dirname(os.path.realpath(__file__))

	# Check if the folder exists, and create it if necessary.
	# http://stackoverflow.com/a/273227/5415895
	if not os.path.exists(folder):
		os.makedirs(folder)

	renderer = Renderer(this_path, __name__)

	renderer.render("CMakeLists.txt", "CMakeLists.txt", folder, {"project": project})
	renderer.render("main.cpp", "main.cpp", folder, {})
	renderer.render("README.md", "README.md", folder, {"project": project})
#}