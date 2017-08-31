import sys
import os
from ..render import Renderer

def create_project(project, folder):
	this_path = os.path.dirname(os.path.realpath(__file__))

	# Check if the folder exists, and create it if necessary.
	# http://bit.ly/2wl5jkU
	if not os.path.exists(folder):
		os.makedirs(folder)
	if not os.path.exists(folder + "/templates"):
		os.mkdir(folder + "/templates")	
	
	renderer = Renderer(this_path, __name__)

	renderer.render('index.php', "index.php", folder, {})
	renderer.render("README.md", "README.md", folder, {"project": project})
	renderer.render("header.php", "templates/header.php", folder, {})
	renderer.render("header.php", "templates/footer.php", folder, {})
	renderer.render('run.sh', "run.sh", folder, {})

	print("Don't forget to run composer init!")