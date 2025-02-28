# Classification (U)

"""Program:  gitmerge_is_remote_branch.py

    Description:  Unit testing of gitmerge.is_remote_branch in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_is_remote_branch.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import collections
import git

# Local
sys.path.append(os.getcwd())
import git_class                                # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def rev_parse2(arg1, branch):

    """Function:  rev_parse2

    Description:  Method stub holder for git.Repo.git.rev_parse().

    Arguments:

    """

    if arg1 and branch:
        raise git.exc.GitCommandError(                  # pylint:disable=E1101
            'git', 128)


def rev_parse(arg1, branch):

    """Function:  rev_parse

    Description:  Method stub holder for git.Repo.git.rev_parse().

    Arguments:

    """

    return bool(arg1) and bool(branch)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_is_remote_branch_false
        test_is_remote_branch_true

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

    def test_is_remote_branch_false(self):

        """Function:  test_is_remote_branch_false

        Description:  Test with exception raised from ls_remote call.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'rev_parse')
        self.gitr.gitcmd = giti(rev_parse2)

        self.assertFalse(self.gitr.is_remote_branch("Branch"))

    def test_is_remote_branch_true(self):

        """Function:  test_is_remote_branch_true

        Description:  Test with successful ls_remote call.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'rev_parse')
        self.gitr.gitcmd = giti(rev_parse)

        self.assertTrue(self.gitr.is_remote_branch("Branch"))


if __name__ == "__main__":
    unittest.main()
