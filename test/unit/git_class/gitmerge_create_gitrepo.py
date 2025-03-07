# Classification (U)

"""Program:  gitmerge_create_gitrepo.py

    Description:  Unit testing of gitmerge.create_gitrepo in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_create_gitrepo.py

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
        test_create_gitrepo

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

    @mock.patch("git_class.GitClass.create_repo")
    @mock.patch("git_class.GitClass.create_cmd")
    def test_create_gitrepo(self, mock_gitc, mock_gitr):

        """Function:  test_create_gitrepo

        Description:  Test with default values settings.

        Arguments:

        """

        mock_gitc.return_value = True
        mock_gitr.return_value = True

        self.gitr.create_gitrepo()

        self.assertEqual((self.gitr.git_dir, self.gitr.repo_name,
                          self.gitr.url, self.gitr.mod_branch,
                          self.gitr.branch, self.gitr.remote_info,
                          self.gitr.br_commit),
                         (self.git_dir, self.repo_name, self.url,
                          self.mod_branch, self.branch, None, None))


if __name__ == "__main__":
    unittest.main()
