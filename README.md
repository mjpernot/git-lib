# Python project that contains libraries and classes for Git use.
# Classification (U)

# Description:
  This program is used to interact with local and remote Git repositories and have capbility to merge repositories.

###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Program Description
  * Testing
    - Unit


# Features:
  * Class that initializes and sets up instances to the Python git repository and git command line instances.
  * Class that handles operations of merging a git repository with a remote git repository.


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/gen_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/git-lib.git
```

Install/upgrade system modules.

```
cd git-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Program Descriptions:
### Description: Contains classes and libraries to interact with local and remote Git repositories.


# Testing:

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the git_class.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/git-lib.git
```

Install/upgrade system modules.

```
cd git-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit test runs for git_class.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

### Unit tests
```
cd {Python_Project}/git-lib
test/unit/git_class/gitclass_init.py
test/unit/git_class/gitclass_create_repo.py
test/unit/git_class/gitclass_create_cmd.py
test/unit/git_class/gitmerge_init.py
test/unit/git_class/gitmerge_set_remote.py
test/unit/git_class/gitmerge_rename_br.py
test/unit/git_class/gitmerge_priority_merge.py
test/unit/git_class/gitmerge_is_untracked.py
test/unit/git_class/gitmerge_is_remote.py
test/unit/git_class/gitmerge_is_remote_branch.py
test/unit/git_class/gitmerge_is_dirty.py
test/unit/git_class/gitmerge_is_commits_behind.py
test/unit/git_class/gitmerge_is_commits_ahead.py
test/unit/git_class/gitmerge_git_pu.py
test/unit/git_class/gitmerge_git_fetch.py
test/unit/git_class/gitmerge_git_co.py
test/unit/git_class/gitmerge_create_gitrepo.py
test/unit/git_class/gitmerge_commits_diff.py
test/unit/git_class/gitmerge_process_untracked.py
test/unit/git_class/gitmerge_process_dirty.py
test/unit/git_class/gitmerge_get_untracked.py
test/unit/git_class/gitmerge_get_dirty.py
```

### All unit testing
```
test/unit/git_class/unit_test_run.sh
```

### Code coverage program
```
test/unit/git_class/code_coverage.sh
```

