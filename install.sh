# "Compile" the project into a zip archive, 
# which can apparently be executed by python.
# http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html

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

$TEMP=temp.sh
echo "sudo mv templates /usr/local/bin" > $TEMP

# https://github.com/jordansissel/fpm/wiki
## http://stackoverflow.com/a/1955555/5415895
VERSION=$(python -c "import sys, json; print json.load(sys.stdin)['version']" < package.json)
## http://stackoverflow.com/a/37124240/5415895
fpm -s dir -t deb -n "templates" --after-install $TEMP -d python -v $VERSION templates

rm $TEMP