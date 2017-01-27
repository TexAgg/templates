# "Compile" the project into a zip archive, 
# which can apparently be executed by python.
# http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html
#
# The executable doesn't work.
# Need pkg_resources

# Zip everything.
zip -r templates.zip *
# Insert shebang in zip.
echo '#!/usr/bin/env python' | cat - templates.zip > templates
# Change access.
chmod +x templates
# Copy executable to path.
cp templates /usr/local/bin