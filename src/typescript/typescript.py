import sys
import os
import jinja2
from jinja2 import Template
import pkg_resources
from ..render import Renderer

def create_project(project, folder):
#{
	# Get name for this path.
	# http://stackoverflow.com/a/5137509/5415895
	this_path = os.path.dirname(os.path.realpath(__file__))

	env = jinja2.Environment(
		block_start_string = '\BLOCK{',
		block_end_string = '}',
		variable_start_string = '\VAR{',
		variable_end_string = '}',
		line_statement_prefix = "-%",
		trim_blocks = True,
		autoescape = False,
   		loader = jinja2.FileSystemLoader(this_path)
	)

	# Check if the folder exists, and create it if necessary.
	# http://stackoverflow.com/a/273227/5415895
	if not os.path.exists(folder):
		os.makedirs(folder)
	if not os.path.exists(folder + "/scripts"):
		os.mkdir(folder + "/scripts")

	renderer = Renderer(this_path, __name__)

	renderer.render("tsconfig.json", "tsconfig.json", folder, {})
	renderer.render("main.ts", "main.ts", folder, {})
	renderer.render("build.py", "build.py", folder, {})
	renderer.render("README.md", "README.md", folder, {"project": project})
	renderer.render("package.json", "package.json", folder, {"project": project})
#}