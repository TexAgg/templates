import json
import os
import glob

# Read the tsconfig to get the input files.
with open('tsconfig.json') as data_file:    
    data = json.load(data_file)
ts_files = data['files']

# Compile typescript files.
print("Compiling typescript files")
os.system("tsc")

# http://stackoverflow.com/a/3964691/5415895
os.chdir("build")
js_files = glob.glob("*.js")
# Make dist subdirectory if not made yet.
# http://stackoverflow.com/a/273227/5415895
if not os.path.exists("dist"):
    os.makedirs("dist")
print("Browserifying files")
os.system("browserify " + " ".join(js_files) + " -o dist/bundle.js")

print("compressing files")
os.system("uglifyjs dist/bundle.js -c -m -o dist/bundle.min.js")