# Classification (U)

"""Program:  gitmerge_get_br_name.py

    Description:  Unit testing of gitmerge.get_br_name in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_get_br_name.py

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

        self.active_branch = Name1()


class Name1(object):                            # pylint:disable=R0903,R0205

    """Class:  Name

    Description:  Class stub holder for git.gitrepo.active_branch.name.

    Methods:
        __init__

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:

        """

        self.name = "Branch_Name"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_get_br_name

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

    def test_get_br_name(self):

        """Function:  test_get_br_name

        Description:  Test with default values settings.

        Arguments:

        """

        self.gitr.gitrepo = ActiveBranch()
        self.assertEqual(self.gitr.get_br_name(), "Branch_Name")


if __name__ == "__main__":
    unittest.main()
