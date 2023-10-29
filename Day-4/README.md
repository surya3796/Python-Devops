1. Modules:- group of functions is referred to as a Module

2. Packages:- group of Modules is referred to as a Package

3. PyPI:- It is like a store for python which has all the libraries. We can use "pip" as a command-line tool to install these libraries.
    
    "pip" stands for "Pip Installs Packages". It is the package installer for Python and is used to install and manage packages. Some common pip commands,

    1. pip install <package-name> - to install a package
    2. pip uninstall <package-name> -  to uninstall a package
    3. pip list - lists all the installed packages
    4. pip list | grep <package-name> - to view a specific package details
    5. pip install --upgrade <package-name> - to upgrade a package


4. Virtual Environment:-
    1. Whenever it requires to work on multiple projects on a single machine, we can use V.Env concept
    2. We can setup individual environment to every project so that there wont be any dependency clashes between multiple projects
        -> python -m venv <projectname> = this command creates a virtual env.
        -> source <projectname>/Scripts/activate = this command activates the virtual.env. for the mentioned project name
        -> deactivate = this command helps to quit the current virtual.env. 