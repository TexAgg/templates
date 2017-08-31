# "Compile" the project into a zip archive, 
# which can apparently be executed by python.
# http://bit.ly/2pUwe4m

# Zip required files: http://bit.ly/2pT4J8W.
zip -r templates.zip * -x *.pyc .git\* resources.md templates debian\* test\* *.deb
# Insert shebang in zip.
echo '#!/usr/bin/env python' | cat - templates.zip > templates
# Change access.
chmod +x templates
# Copy executable to path.
sudo cp templates /usr/local/bin
# Delete the zip file.
rm templates.zip

# BETA: create deb package.

TEMP=temp.sh
echo "sudo mv templates /usr/local/bin" > $TEMP

# http://bit.ly/2pQlOlJ
## http://bit.ly/2wLYWrT
VERSION=$(python -c "import sys, json; print json.load(sys.stdin)['version']" < package.json)
## http://bit.ly/2vuLn0q
fpm -s dir -t deb -n "templates" --after-install $TEMP -d python -d jinja2 -v $VERSION --description "Templates and scripts for easily creating projects" --url "https://github.com/TexAgg/templates" --maintainer "mgaikema1@protonmail.com" --license "GPL-3.0" templates

rm $TEMP