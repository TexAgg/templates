import sys
import os
from ..render import Renderer

def create_project(assignment, folder, honor_statement, bib, name):
#{
	# Get name for this path.
	# http://bit.ly/2wVprfh
	this_path = os.path.dirname(os.path.realpath(__file__))

	renderer = Renderer(this_path, __name__)

	# Check if the folder exists, and create it if necessary.
	# http://bit.ly/2wl5jkU
	if not os.path.exists(folder):
		os.makedirs(folder)

	if bib:
		renderer.render("sources.bib", "sources.bib", folder, {})

	renderer.render("main.tex", "main.tex", folder, {"assignment": assignment, "bib": bib, "name": name})
	renderer.render("Makefile", "Makefile", folder, {"bib": bib})
	renderer.render("README.md", "README.md", folder, {"assignment": assignment})
	
	if honor_statement:
		renderer.render("honor.txt", "honor.txt", folder, {})
#}