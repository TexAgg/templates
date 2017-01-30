#!/usr/bin/env python

import sys
import os
import argparse
import src.homework.homework as homework
import src.cpp.cpp as cpp
import src.typescript.typescript as ts

parser = argparse.ArgumentParser(description="Create an empty project.")
subparsers = parser.add_subparsers(help='type of project.', dest='type')
parser.add_argument('-d', "--dir", help="The directory where the project should be.", required=True)
parser.add_argument('-t', '--title', help="Title of the project being made", required=True)

# C++ subparser.
cpp_parser = subparsers.add_parser('cpp', help='Make a C++ project')

# Homework subparser.
hw_subparser = subparsers.add_parser('homework', help="Make a homework document")
hw_subparser.add_argument('--honor', action='store_true' ,help="Whether to include the Aggie Honor Statement.")

# Typescript subparser.
ts_subparser = subparsers.add_parser('ts', help="Make a homework document")

args = vars(parser.parse_args())

if args['type'] == "cpp":
	cpp.create_project(args['title'], args['dir'])
elif args['type'] == "homework":
	homework.create_project(args['title'], args['dir'], args['honor'])
elif args['type'] == 'ts':
	ts.create_project(args['title'], args['dir'])