# Classification (U)

"""Program:  gitconfig_set_user.py

    Description:  Unit testing of gitconfig.set_user in git_class.py.

    Usage:
        test/unit/git_class/gitconfig_set_user.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil
import unittest

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
        test_set_user
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.user = "user_name"
        self.repo_dir = "test/unit/git_class/test/test-repo"
        self.gitr = git_class.GitConfig(self.repo_dir)

    def test_set_user(self):

        """Function:  test_set_user

        Description:  Test set_user method.

        Arguments:

        """

        self.gitr.set_user(self.user)
        gita = git_class.GitConfig(self.repo_dir)

        self.assertEqual(gita.get_user(), self.user)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of unit testing.

        Arguments:

        """

        if os.path.isdir(self.repo_dir):
            shutil.rmtree(self.repo_dir)


if __name__ == "__main__":
    unittest.main()
