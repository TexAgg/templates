#!/usr/bin/env python

import sys
import os
import argparse
import src.homework.homework as homework
import src.cpp.cpp as cpp
import src.typescript.typescript as ts
import json

# Read the version from the package.json.
with open('package.json') as json_data:
	d = json.load(json_data)
	version = d['version']

parser = argparse.ArgumentParser(description="Create an empty project.", prog="templates")
subparsers = parser.add_subparsers(help='type of project.', dest='type')
parser.add_argument('-d', "--dir", help="The directory where the project should be.", required=True)
parser.add_argument('-t', '--title', help="Title of the project being made", required=True)
parser.add_argument('--version', action='version', version='%(prog)s ' + version)

# C++ subparser.
cpp_parser = subparsers.add_parser('cpp', help='Make a C++ project')

# Homework subparser.
hw_subparser = subparsers.add_parser('homework', help="Make a homework document")
hw_subparser.add_argument('--honor', action='store_true', help="Whether to include the Aggie Honor Statement.")
hw_subparser.add_argument("--bib", action="store_true", help="Include a bibliography")

# Typescript subparser.
ts_subparser = subparsers.add_parser('ts', help="Make a homework document")
#ts_subparser.add_argument("-w", "--webpack", action="store_true", help="Whether to use Webpack for the bundling.")

args = vars(parser.parse_args())

if args['type'] == "cpp":
	cpp.create_project(args['title'], args['dir'])
elif args['type'] == "homework":
	homework.create_project(args['title'], args['dir'], args['honor'], args['bib'])
elif args['type'] == 'ts':
	ts.create_project(args['title'], args['dir'])