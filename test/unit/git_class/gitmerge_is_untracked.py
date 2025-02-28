# Classification (U)

"""Program:  gitmerge_is_untracked.py

    Description:  Unit testing of gitmerge.is_untracked in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_is_untracked.py

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


def is_untracked2(untracked_files):

    """Function:  is_untracked2

    Description:  Method stub holder for git.Repo.git.is_untracked().

    Arguments:

    """

    status = False

    return status if untracked_files else False


def is_untracked(untracked_files):

    """Function:  is_untracked

    Description:  Method stub holder for git.Repo.git.is_untracked().

    Arguments:

    """

    status = True

    return status if untracked_files else True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_is_untracked_false
        test_is_untracked_true

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

    def test_is_untracked_false(self):

        """Function:  test_is_untracked_false

        Description:  Test with is_untracked returns False.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'is_dirty')
        self.gitr.gitrepo = giti(is_untracked2)

        self.assertFalse(self.gitr.is_untracked())

    def test_is_untracked_true(self):

        """Function:  test_is_untracked_true

        Description:  Test with is_untracked returns True.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'is_dirty')
        self.gitr.gitrepo = giti(is_untracked)

        self.assertTrue(self.gitr.is_untracked())


if __name__ == "__main__":
    unittest.main()
