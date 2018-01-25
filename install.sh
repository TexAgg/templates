# "Compile" the project into a zip archive, 
# which can apparently be executed by python.
# http://bit.ly/2pUwe4m

# Zip required files: http://bit.ly/2pT4J8W.
zip -r templates.zip * -x *.pyc .git\* resources.md templates debian\* test\* *.deb .vscode\*
# Insert shebang in zip.
echo '#!/usr/bin/env python' | cat - templates.zip > templates
# Change access.
chmod +x templates
# Copy executable to path.
sudo cp templates /usr/local/bin
# Delete the zip file.
rm templates.zip

MANPAGE=templates.1
# Create man page from `--help` output.
help2man templates -o ${MANPAGE} --no-discard-stderr
# Save man page in the place where man pages are saved.
sudo cp $MANPAGE /usr/local/man/man1
# Since running `npm version *` updates the version and then creates a tag,
# the version given in the manpage will always be behind, unless I manually
# update it before release.


# Create deb package.
# This will not install it.

# Create temporary directory for packaging.
TEMPDIR=$(mktemp -d -p .)
mkdir -p $TEMPDIR/usr/local/man/man1
cp -t $TEMPDIR/usr/local/man/man1 $MANPAGE
mkdir -p $TEMPDIR/usr/local/bin
cp -t $TEMPDIR/usr/local/bin templates

# FPM: http://bit.ly/2pQlOlJ
## Parse version field from project.json: http://bit.ly/2wLYWrT
VERSION=$(python -c "import sys, json; print json.load(sys.stdin)['version']" < package.json)
## http://bit.ly/2vuLn0q
fpm -s dir -t deb -C $TEMPDIR -n "templates" -d python2.7 \
	-d python-jinja2 -v $VERSION \
	--description "Templates and scripts for easily creating projects" \
	--url "https://github.com/TexAgg/templates" \
	--maintainer "mgaikema1@protonmail.com" --license "GPL-3.0" \
	.

rm -r $TEMPDIR