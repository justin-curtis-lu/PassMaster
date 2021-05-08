# Pass Master

Application allows user to store and edit their passwords. Main interface is a table which allows for Name, User, Password, and URL tracking for each associated password. 

GUI built using PyQt5, with Sqlite serving as the database. Pyinstaller used to build the application, with InstallForge used to create an installer.

## Getting Started

The application can be run in two ways

1) Download the installer
2) Clone the Repo

### 1 Download the installer

https://drive.google.com/file/d/1JexiLHfAcwAGK04MVaAajFefNXRzGRwB/view?usp=sharing

Run the installer, which should create a shortcut for the application which you can then run.

#### OR 

### 2 Clone the Repo

If deciding to clone the repo, first ensure that dependencies are satisfied by typing

```
pip install -r requirements.txt
```
into a terminal. Then simply run 
```
py passmaster.py
```
in the correct directory.

## Built With

* [PyQt5](https://pypi.org/project/PyQt5/) - Graphical User Interface
* [Sqlite](https://het.as.utexas.edu/HET/Software/PyQt/qtsql.html) - Primary Database
* [Pyinstaller](https://pypi.org/project/pyinstaller/) - Bundling the Python application and dependencies into single package
* [InstallForge](https://installforge.net/download/) - Installion Builder
