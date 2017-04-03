import sys
import os
from ..render import Renderer

def create_project(assignment, folder, honor_statement, bib):
#{
	# Get name for this path.
	# http://stackoverflow.com/a/5137509/5415895
	this_path = os.path.dirname(os.path.realpath(__file__))

	renderer = Renderer(this_path, __name__)

	# Check if the folder exists, and create it if necessary.
	# http://stackoverflow.com/a/273227/5415895
	if not os.path.exists(folder):
		os.makedirs(folder)

	if bib:
		renderer.render("sources.bib", "sources.bib", folder, {})

	renderer.render("main.tex", "main.tex", folder, {"assignment": assignment, "bib": bib})
	renderer.render("Makefile", "Makefile", folder, {"bib": bib})
	renderer.render("README.md", "README.md", folder, {"assignment": assignment})
	
	if honor_statement:
		renderer.render("honor.txt", "honor.txt", folder, {})
#}