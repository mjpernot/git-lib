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
import unittest

# Local
sys.path.append(os.getcwd())
import git_class                                # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ActiveBranch(object):                     # pylint:disable=R0903,R0205

    """Class:  ActiveBranch

    Description:  Class stub holder for git.gitrepo.active_branch.

    Methods:
        __init__

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        self.active_branch = Commit1()


class Commit1(object):                          # pylint:disable=R0903,R0205

    """Class:  Commit1

    Description:  Class stub holder for git.gitrepo.active_branch.commit.

    Methods:
        __init__

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        self.commit = Hexsha1()


class Hexsha1(object):                          # pylint:disable=R0903,R0205

    """Class:  Hexsha1

    Description:  Class stub holder - git.gitrepo.active_branch.commit.hexsha.

    Methods:
        __init__

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        self.hexsha = "1234567890abcdef"


class Checkout1(object):                        # pylint:disable=R0903,R0205

    """Class:  Checkout1

    Description:  Class stub holder for git.gitrepo.Git.checkout.

    Methods:
        __init__
        checkout

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

    def checkout(self, branch):

        """Function:  checkout

        Description:  Method stub holder for git.gitrepo.Git.checkout().

        Arguments:
            branch

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_detach_head

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
        self.gitr.gitcmd = Checkout1()
        self.assertFalse(self.gitr.detach_head())


if __name__ == "__main__":
    unittest.main()
