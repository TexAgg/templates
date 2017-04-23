# "Compile" the project into a zip archive, 
# which can apparently be executed by python.
# http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html

# Zip required files: http://bit.ly/2pT4J8W.
zip -r templates.zip * -x *.pyc .git\* resources.md templates debian\* test\*
# Insert shebang in zip.
echo '#!/usr/bin/env python' | cat - templates.zip > templates
# Change access.
chmod +x templates
# Copy executable to path.
sudo cp templates /usr/local/bin
# Delete the zip file.
rm templates.zip
