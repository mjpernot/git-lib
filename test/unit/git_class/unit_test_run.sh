#!/bin/bash
# Unit testing program for the git_class.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  git_class.py"
/usr/bin/python test/unit/git_class/gitmerge_init.py
/usr/bin/python test/unit/git_class/gitmerge_detach_head.py
/usr/bin/python test/unit/git_class/gitmerge_get_br_name.py
/usr/bin/python test/unit/git_class/gitmerge_remove_branch.py
/usr/bin/python test/unit/git_class/gitmerge_create_gitrepo.py
/usr/bin/python test/unit/git_class/gitmerge_set_remote.py
/usr/bin/python test/unit/git_class/gitmerge_is_remote.py
/usr/bin/python test/unit/git_class/gitmerge_process_dirty.py
/usr/bin/python test/unit/git_class/gitmerge_process_untracked.py
/usr/bin/python test/unit/git_class/gitmerge_is_dirty.py
/usr/bin/python test/unit/git_class/gitmerge_is_untracked.py
/usr/bin/python test/unit/git_class/gitmerge_git_fetch.py
/usr/bin/python test/unit/git_class/gitmerge_rename_br.py
/usr/bin/python test/unit/git_class/gitmerge_git_co.py
/usr/bin/python test/unit/git_class/gitmerge_priority_merge.py
/usr/bin/python test/unit/git_class/gitmerge_git_pu.py
/usr/bin/python test/unit/git_class/gitmerge_commits_diff.py
/usr/bin/python test/unit/git_class/gitmerge_is_commits_ahead.py
/usr/bin/python test/unit/git_class/gitmerge_is_commits_behind.py
/usr/bin/python test/unit/git_class/gitmerge_is_remote_branch.py
/usr/bin/python test/unit/git_class/gitmerge_get_dirty.py
/usr/bin/python test/unit/git_class/gitmerge_get_untracked.py
/usr/bin/python test/unit/git_class/gitclass_init.py
/usr/bin/python test/unit/git_class/gitclass_create_repo.py
/usr/bin/python test/unit/git_class/gitclass_create_init.py
/usr/bin/python test/unit/git_class/gitclass_create_cmd.py
/usr/bin/python test/unit/git_class/gitconfig_init.py
/usr/bin/python test/unit/git_class/gitconfig_get_email.py
/usr/bin/python test/unit/git_class/gitconfig_get_user.py
/usr/bin/python test/unit/git_class/gitconfig_set_email.py
/usr/bin/python test/unit/git_class/gitconfig_set_user.py

