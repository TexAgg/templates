import sys
import os
# http://bit.ly/2vvesJ0
from ..render import Renderer

def create_project(project, folder):
#{
	# Get name for this path.
	# http://bit.ly/2wVprfh
	this_path = os.path.dirname(os.path.realpath(__file__))

	# Check if the folder exists, and create it if necessary.
	# http://bit.ly/2wl5jkU
	if not os.path.exists(folder):
		os.makedirs(folder)

	renderer = Renderer(this_path, __name__)

	renderer.render("CMakeLists.txt", "CMakeLists.txt", folder, {"project": project})
	renderer.render("main.cpp", "main.cpp", folder, {})
	renderer.render("README.md", "README.md", folder, {"project": project})
#}