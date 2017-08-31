# Reads the files in tsconfig.json, compiles them to javascript,
# and then browserifies and uglifies the javascript.
# The newest version of this file can be found at <https://pastebin.com/JVD1rn2a>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

# http://bit.ly/2wVwmFc
os.chdir("build")
js_files = glob.glob("*.js")
# Make dist subdirectory if not made yet.
# http://bit.ly/2wl5jkU
if not os.path.exists("dist"):
    os.makedirs("dist")
print("Browserifying files")
os.system("browserify " + " ".join(js_files) + " -o dist/bundle.js")

print("Compressing files")
os.system("uglifyjs dist/bundle.js -c -m -o dist/bundle.min.js")

print("Done")
