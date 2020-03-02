#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_remove_branch.py

    Description:  Unit testing of gitmerge.remove_branch in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_remove_branch.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock
import collections

# Local
sys.path.append(os.getcwd())
import git_class
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class DeleteHead(object):

    """Class:  DeleteHead

    Description:  Class stub holder for git.gitrepo.delete_head.

    Methods:
        delete_head -> Stub holder for git.gitrepo.delete_head method.

    """

    def delete_head(self, branch):

        """Function:  delete_head

        Description:  Stub holder for git.gitrepo.delete_head method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_other_branch -> Test with removing another branch.
        test_current_branch -> Test with removing current branch.

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
        self.branch_name = "Branch_Name"
        self.error_msg = "WARNING: Cannot remove branch if current branch."

        self.gitr = git_class.GitMerge(self.repo_name, self.git_dir, self.url,
                                       self.branch, self.mod_branch)

    @mock.patch("git_class.GitMerge.get_br_name",
                mock.Mock(return_value="New_Branch"))
    def test_other_branch(self):

        """Function:  test_other_branch

        Description:  Test with removing another branch.

        Arguments:

        """

        self.gitr.gitrepo = DeleteHead()
        self.assertEqual(self.gitr.remove_branch(self.branch_name),
                         (True, None))

    @mock.patch("git_class.GitMerge.get_br_name",
                mock.Mock(return_value="Branch_Name"))
    def test_current_branch(self):

        """Function:  test_current_branch

        Description:  Test with removing current branch.

        Arguments:

        """

        self.assertEqual(self.gitr.remove_branch(self.branch_name),
                         (False, self.error_msg))


if __name__ == "__main__":
    unittest.main()
