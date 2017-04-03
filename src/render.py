import sys
import os
import jinja2
from jinja2 import Template
import pkg_resources

class Renderer():

	def __init__(self, template_dir, name):
		self.name = name
		self.template_dir = template_dir
		self.env = jinja2.Environment(
			block_start_string = '\BLOCK{',
			block_end_string = '}',
			variable_start_string = '\VAR{',
			variable_end_string = '}',
			line_statement_prefix = "-%",
			trim_blocks = True,
			autoescape = False,
			loader = jinja2.FileSystemLoader(template_dir)
		)

	def render(self, infile, outfile, folder, args):
		file_template = self.env.from_string(pkg_resources.resource_string(self.name, infile))
		file_string = file_template.render(args = args)
		with open(folder + "/" + outfile, "w+") as f:
			f.write(file_string)