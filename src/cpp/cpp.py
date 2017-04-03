import sys
import os
import jinja2
from jinja2 import Template
import pkg_resources
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

	renderer.render("CMakeLists.txt", "CMakeLists.txt", folder, {"project": project})
	renderer.render("main.cpp", "main.cpp", folder, {})
	renderer.render("README.md", "README.md", folder, {"project": project})
#}