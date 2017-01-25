import sys
import os
import jinja2
from jinja2 import Template

def create_project(assignment, folder, honor_statement):
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

	tex_template = env.get_template('main.tex')
	tex_string = tex_template.render(assignment = assignment)
	with open(folder + "/main.tex", "w+") as f:
  		f.write(tex_string)
	
	make_template = env.get_template('Makefile')
	make_string = make_template.render()
	with open(folder + "/Makefile", "w+") as f:
  		f.write(make_string)

	readme_template = env.get_template('README.md')
	readme_string = readme_template.render(assignment = assignment)
	with open(folder + "/README.md", "w+") as f:
  		f.write(readme_string)
	
	if honor_statement:
		honor_template = env.get_template('honor.txt')
		honor_string = honor_template.render()
		with open(folder + "/honor.txt", "w+") as f:
			f.write(honor_string)
#}