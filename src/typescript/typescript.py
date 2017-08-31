import sys
import os
from ..render import Renderer

def create_project(project, folder, no_webpack):
#{
	# Get name for this path.
	# http://bit.ly/2wVprfh
	this_path = os.path.dirname(os.path.realpath(__file__))

	# Check if the folder exists, and create it if necessary.
	# http://bit.ly/2wl5jkU
	if not os.path.exists(folder):
		os.makedirs(folder)
	if not os.path.exists(folder + "/scripts"):
		os.mkdir(folder + "/scripts")

	renderer = Renderer(this_path, __name__)

	renderer.render("tsconfig.json", "tsconfig.json", folder, {})
	# http://bit.ly/2glJp8b
	renderer.render("main.ts", "scripts/main.ts", folder, {})
	renderer.render("README.md", "README.md", folder, {"project": project})
	if (not no_webpack):
		# http://bit.ly/2nHluCr
		renderer.render("webpack.config.js", "webpack.config.js", folder, {})
		print("Don't forget to run `yarn init` and `yarn add --dev tsc-loader`!")
	else:
		renderer.render("build.py", "build.py", folder, {})
#}
