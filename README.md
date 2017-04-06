# Templates
Various templates I use for easily creating projects.
The app will create projects assuming that your name is "Matt Gaikema", which has worked fine for me, but if you have a different name you might need to do some tinkering.

---

## Usage
```
templates.py -t <project> -d <directory> <type>
```
creates a `<type>` project named `<project>` in the directory `<directory>`.
Run `python templates.py -h` for more help.

### Installation
Run `bash install.sh` (`sudo` will be prompted as needed) and the script will be installed to your `PATH` so you can call `templates` anywhere in your terminal.
You might need to install the dependencies with [`pip install -r requirements.txt`](http://stackoverflow.com/a/10429168/5415895).

---

## Resources
* [Command Line Arguments](https://docs.python.org/2/library/optparse.html)
* [ZIP executable](http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html)
