# Classification (U)

"""Program:  gitmerge_is_commits_behind.py

    Description:  Unit testing of gitmerge.is_commits_behind in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_is_commits_behind.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import git_class                                # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_commitsdiff_zero
        test_commitsdiff_one
        test_commitsdiff_two

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

    @mock.patch("git_class.GitMerge.commits_diff")
    def test_commitsdiff_zero(self, mock_commit):

        """Function:  test_commitsdiff_zero

        Description:  Test with zero commits difference.

        Arguments:

        """

        mock_commit.return_value = 0

        self.assertEqual(self.gitr.is_commits_behind("Data"), 0)

    @mock.patch("git_class.GitMerge.commits_diff")
    def test_commitsdiff_one(self, mock_commit):

        """Function:  test_commitsdiff_one

        Description:  Test with one commit difference.

        Arguments:

        """

        mock_commit.return_value = 1

        self.assertEqual(self.gitr.is_commits_behind("Data"), 1)

    @mock.patch("git_class.GitMerge.commits_diff")
    def test_commitsdiff_two(self, mock_commit):

        """Function:  test_commitsdiff_two

        Description:  Test with two commits difference.

        Arguments:

        """

        mock_commit.return_value = 2

        self.assertEqual(self.gitr.is_commits_behind("Data"), 2)


if __name__ == "__main__":
    unittest.main()
