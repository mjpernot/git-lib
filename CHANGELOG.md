# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [1.0.4] - 2022-12-16
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4

### Changed
- Modified exception handler to Python 3 format.


## [1.0.3] - 2022-06-28
- Number of minor fixes in support files.
- Documentation updates.

## [1.0.2] - 2022-02-11
- Number of minor fixes in support files.
- Documentation updates.


## [1.0.1] - 2021-11-01
### Changed
- Documentation updates.


## [1.0.0] - 2021-03-09
- General Release

### Changed
- GitMerge.priority_merge:  Add option to merge unrelated git histories.
- Removed uncessary \*\*kwargs from methods function paramters.


## [0.3.1] - 2020-03-27
### Fixed
- GitMerge.remove_branch:  Added no_chk argument to suspend checking of current branch.


## [0.3.0] - 2020-02-24
### Added
- GitMerge.remove_branch:  Added method to remove branch name passed to method.
- GitMerge.get_br_name:  Added method to return the current branch name.
- GitMerge.detach_head:  Added method to checkout the head to the latest Commit ID.


## [0.2.0] - 2019-09-24
### Fixed
- GitMerge.process_untracked:  Allow for the removal of untracked directories.


## [0.1.2] - 2019-06-12
### Changed
- GitClass.\_\_init\_\_:  Added attribute for git.Repo.init class.
- GitMerge.priority_merge:  Captured standard error out in the exception handler.

### Added
- GitConfig:  Create a create a git.Repo.init class.
- GitClass.create_init:  Create a git.Repo.init instance.


## [0.1.1] - 2019-06-04
### Added
- \_\_init\_\_.py:  Added file for class use.

### Changed
- setup.py:  Added py_modules section.


## [0.1.0] - 2019-05-14
- Initial creation.

