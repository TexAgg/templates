# Homework template
An M4 macro for creating an empty homework assignment,
which consists of an empty Tex file with the appropriate title,
and a Makefile for it.

---

## Instructions
The script `homework.py` takes two command line arguments,
the assignment title, and the folder to create.

For example,
to create an assignment called "Math 446 hw3" in the directory `/home/matt/Dropbox/College/2016-2017/Fall/Math-446/hw3`,
call 
```
$ python homework.py "Math 446 hw3" /home/matt/Dropbox/College/2016-2017/Fall/Math-446/hw3
```