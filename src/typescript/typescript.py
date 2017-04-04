import sys
import os
from ..render import Renderer

def create_project(project, folder, webpack):
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

	renderer = Renderer(this_path, __name__)

	renderer.render("tsconfig.json", "tsconfig.json", folder, {})
	# http://stackoverflow.com/a/8858026/5415895
	renderer.render("main.ts", "scripts/main.ts", folder, {})
	renderer.render("README.md", "README.md", folder, {"project": project})
	renderer.render("package.json", "package.json", folder, {"project": project})
	if (webpack):
		# http://bit.ly/2nHluCr
		renderer.render("webpack.config.js", "webpack.config.js", folder, {})
		print("Don't forget to run `yarn add --dev tsc-loader`!")
	else:
		renderer.render("build.py", "build.py", folder, {})
#}