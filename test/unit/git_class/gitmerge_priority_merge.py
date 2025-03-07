# Classification (U)

"""Program:  gitmerge_priority_merge.py

    Description:  Unit testing of gitmerge.priority_merge in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_priority_merge.py

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


def merge2(arg_list):

    """Function:  merge

    Description:  Method stub holder for git.Repo.git.merge().

    Arguments:

    """

    if arg_list:
        raise git.exc.GitCommandError(                  # pylint:disable=E1101
            "git", 128, "stderr")


def merge(arg_list):

    """Function:  merge

    Description:  Method stub holder for git.Repo.git.merge().

    Arguments:

    """

    status = True

    if arg_list:
        status = True

    return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_allow_branch_options
        test_allow_option
        test_priority_merge_branch
        test_priority_merge_exception
        test_priority_merge_true

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

    def test_allow_branch_options(self):

        """Function:  test_allow_branch_options

        Description:  Test with allow and branch parameters.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = giti(merge)

        status, msg = self.gitr.priority_merge(ranch="New_Branch", allow=True)
        self.assertEqual((status, msg), (True, {}))

    def test_allow_option(self):

        """Function:  test_allow_option

        Description:  Test with allow parameter passed.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = giti(merge)

        status, msg = self.gitr.priority_merge(allow=True)
        self.assertEqual((status, msg), (True, {}))

    def test_priority_merge_branch(self):

        """Function:  test_priority_merge_branch

        Description:  Test with branch parameter passed.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = giti(merge)

        status, msg = self.gitr.priority_merge(branch="New_Branch")
        self.assertEqual((status, msg), (True, {}))

    def test_priority_merge_exception(self):

        """Function:  test_priority_merge_exception

        Description:  Test with raised exception.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = giti(merge2)

        status, msg = self.gitr.priority_merge()
        self.assertEqual((status, msg["status"]), (False, 128))

    def test_priority_merge_true(self):

        """Function:  test_priority_merge_true

        Description:  Test with successful branch call.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'merge')
        self.gitr.gitcmd = giti(merge)

        status, msg = self.gitr.priority_merge()
        self.assertEqual((status, msg), (True, {}))


if __name__ == "__main__":
    unittest.main()
