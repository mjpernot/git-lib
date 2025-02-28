# Classification (U)

"""Program:  gitmerge_set_remote.py

    Description:  Unit testing of gitmerge.set_remote in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_set_remote.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import collections

# Local
sys.path.append(os.getcwd())
import git_class                                # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def remote(arg1, arg2, arg3):

    """Function:  remote

    Description:  Method stub holder for git.Repo.git.remote().

    Arguments:

    """

    return bool(arg1) and bool(arg2) and bool(arg3)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_set_remote

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

    def test_set_remote(self):

        """Function:  test_set_remote

        Description:  Test with default values settings.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'remote')
        self.gitr.gitcmd = giti(remote)

        self.assertFalse(self.gitr.set_remote())


if __name__ == "__main__":
    unittest.main()
