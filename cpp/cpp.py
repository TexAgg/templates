import sys
import os
import jinja2
from jinja2 import Template

def create_project(project, folder):
#{
	# Get name for this path.
	# http://stackoverflow.com/a/5137509/5415895
	this_path = os.path.dirname(os.path.realpath(__file__))

	# Check if the folder exists, and create it if necessary.
	# http://stackoverflow.com/a/273227/5415895
	if not os.path.exists(folder):
		os.makedirs(folder)

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

	cmake_template = env.get_template('CMakeLists.txt')
	cmake_string = cmake_template.render(project = project)
	with open(folder + "/CMakeLists.txt", "w+") as f:
		f.write(cmake_string)

	cpp_template = env.get_template('main.cpp')
	cpp_string = cpp_template.render()
	with open(folder + "/main.cpp", "w+") as f:
		f.write(cpp_string)

	readme_template = env.get_template('README.md')
	readme_string = readme_template.render(project = project)
	with open(folder + "/README.md", "w+") as f:
		f.write(readme_string)
#}