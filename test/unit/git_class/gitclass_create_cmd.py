# Classification (U)

"""Program:  gitclass_create_cmd.py

    Description:  Unit testing of GitClass.create_cmd in git_class.py.

    Usage:
        test/unit/git_class/gitclass_create_cmd.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_repodir_not_set
        test_repodir_set

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gitc = git_class.GitClass()

    def test_repodir_not_set(self):

        """Function:  test_repodir_not_set

        Description:  Test with repo_dir attribute not set.

        Arguments:

        """

        self.gitc.create_cmd()

        self.assertEqual((self.gitc.gitcmd, self.gitc.repo_dir), (None, "."))

    def test_repodir_set(self):

        """Function:  test_repodir_set

        Description:  Test with repo_dir attribute set.

        Arguments:

        """

        giti = collections.namedtuple('GIT', 'git')
        self.gitc.gitrepo = giti("Cmd Instance")

        self.gitc.create_cmd()

        self.assertEqual((self.gitc.gitcmd, self.gitc.repo_dir),
                         ("Cmd Instance", "."))


if __name__ == "__main__":
    unittest.main()
