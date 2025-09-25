# Python project that contains libraries and classes for Git repository use.
# Classification (U)

# Description:
  This project is used to interact with local and remote Git repositories and have capbility to merge repositories.  It contains classes and libraries for both local and remote Git repositories.

###  This README file is broken down into the following sections:
  * Prerequisites
  * Installation
    - Pip Installation
  * Testing
    - Git Installation
    - Unit


# Prerequisites:

  * List of Linux packages that need to be installed on the server via git.
    - python3-pip


# Installation:

### Pip Installation:

##### Create requirements file in another program's project to install git-lib as a library module.

  * Create requirements-git-lib.txt and requirements-git-python-lib.txt.  Replace N.N.N with the version of the library needed.

```
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/git-lib.git@N.N.N#egg=mysql-lib' > requirements-git-lib.txt
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git@N.N.N#egg=python-lib' > requirements-git-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file and the following lines to install the library modules:

```
python -m pip install -r requirements-git-lib.txt --target git_lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-git-python-lib.txt --target git_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general git-Lib requirements (requirements3.txt) to the other program's requirements3.txt file.


# Testing:

### Git Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/git-lib.git
```

Install/upgrade system modules:

NOTE: Install as the user that will use the package.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```


Install supporting classes and libraries:

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit Testing:

### Installation:

Install the project using the procedures in the Git Installation section.

### Testing:

```
test/unit/git_class/unit_test_run.sh
test/unit/git_class/code_coverage.sh
```

