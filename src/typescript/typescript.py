import sys
import os
import jinja2
from jinja2 import Template
import pkg_resources

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

	tsconfig_template = env.from_string(pkg_resources.resource_string(__name__, 'tsconfig.json'))
	tsconfig_string = tsconfig_template.render()
	with open(folder + "/tsconfig.json", "w+") as f:
		f.write(tsconfig_string)

	main_template = env.from_string(pkg_resources.resource_string(__name__, 'main.ts'))
	main_string = main_template.render()
	with open(folder + "/main.ts", "w+") as f:
		f.write(main_string)

	build_template = env.from_string(pkg_resources.resource_string(__name__, 'build.py'))
	build_string = build_template.render()
	with open(folder + "/build.py", "w+") as f:
		f.write(build_string)

	readme_template = env.from_string(pkg_resources.resource_string(__name__, 'README.md'))
	readme_string = readme_template.render(project = project)
	with open(folder + "/README.md", "w+") as f:
		f.write(readme_string)

	package_template = env.from_string(pkg_resources.resource_string(__name__, 'package.json'))
	package_string = package_template.render(project = project)
	with open(folder + "/package.json", "w+") as f:
		f.write(package_string)
#}