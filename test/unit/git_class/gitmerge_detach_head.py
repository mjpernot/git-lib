#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_detach_head.py

    Description:  Unit testing of gitmerge.detach_head in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_detach_head.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock
import collections

# Local
sys.path.append(os.getcwd())
import git_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ActiveBranch(object):

    """Class:  Index

    Description:  Class stub holder for git.gitrepo.index.

    Methods:
        __init -> Class initilization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        self.active_branch = Commit()


class Commit(object):

    """Class:  Diff

    Description:  Class stub holder for git.gitrepo.index.diff.

    Methods:
        __init -> Class initilization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        self.commit = Hexsha()


class Hexsha(object):

    """Class:  Diff

    Description:  Class stub holder for git.gitrepo.index.diff.

    Methods:
        __init -> Class initilization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        self.hexsha = "1234567890abcdef"


class Checkout(object):

    """Class:  Diff

    Description:  Class stub holder for git.gitrepo.index.diff.

    Methods:
        __init -> Class initilization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        pass


    def checkout(self, branch):

        """Function:  checkout

        Description:  Method stub holder for git.Repo.git.checkout().

        Arguments:
            branch -> Stub holder for branch name or hexi-Commit ID.

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_detach_head -> Test with default values settings.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.repo_name = "Repo_name"
        self.git_dir = "/directory/git"
        self.url = "URL"
        self.branch = "Remote_branch"
        self.mod_branch = "Mod_branch"

        self.gitr = git_class.GitMerge(self.repo_name, self.git_dir, self.url,
                                       self.branch, self.mod_branch)

    def test_detach_head(self):

        """Function:  test_detach_head

        Description:  Test with default values settings.

        Arguments:

        """

        self.gitr.gitrepo = ActiveBranch()
        self.gitr.gitcmd = Checkout()
        self.assertFalse(self.gitr.detach_head())


if __name__ == "__main__":
    unittest.main()
