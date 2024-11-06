# Python project that contains libraries and classes for Git repository use.
# Classification (U)

# Description:
  This project is used to interact with local and remote Git repositories and have capbility to merge repositories.  It contains classes and libraries for both local and remote Git repositories.

###  This README file is broken down into the following sections:
  * Installation
    - Pip Installation
    - Git Installation
  * Testing
    - Unit


# Installation:
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.
  * Replace any reference to **{Other_Python_Project}** with the baseline path of another python program.
  * There are two types of installs: pip and git.

### Pip Installation:

##### Create requirements file in another program's project to install git-lib as a library module.

Create requirements-git-lib.txt file and requirements-python-lib.txt files:

```
cp {Python_Project}/requirements-git-lib.txt {Other_Python_Project}/requirements-git-lib.txt
cp {Python_Project}/requirements-python-lib.txt {Other_Python_Project}/requirements-git-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the {Other_Python_Project}/README.md file:

Centos 7 (Running Python 2.7):
```
pip install -r requirements-git-lib.txt --target git_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-git-python-lib.txt --target git_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
```
python -m pip install -r requirements-git-lib.txt --target git_lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-git-python-lib.txt --target git_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


##### Add the general Git-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Add/modify the following lines to the {Other_Python_Project}/requirements.txt file:

Centos 7 (Running Python 2.7):
{Python_Project}/requirements.txt

Redhat 8 (Running Python 3.6):
{Python_Project}/requirements3.txt


### Git Installation:

Install general Git-lib libraries and classes using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/git-lib.git
cd git-lib
```

Install/upgrade system modules:

Centos 7 (Running Python 2.7):
```
sudo pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
NOTE: Install as the user that will use the package.

```
python -m pip install --user -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```


Install supporting classes and libraries:

Centos 7 (Running Python 2.7):
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```



# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Git Installation section.

### Testing:

```
cd {Python_Project}/git-lib
test/unit/git_class/unit_test_run3.sh
```

### Code Coverage:

```
cd {Python_Project}/git-lib
test/unit/git_class/code_coverage.sh
```

