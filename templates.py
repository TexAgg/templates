import sys
import os
import homework.homework as homework
import cpp.cpp as cpp
import typescript.typescript as ts

if sys.argv[1] == "homework":
	homework.create_project(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "cpp":
	cpp.create_project(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "ts":
	ts.create_project(sys.argv[2], sys.argv[3])