#!/bin/sh
#
# Git post-receive hook for deployment.
#
# daniel.simmons@tobias.tv
# 2012-03-29
#

cd "$GIT_DIR/.."

# These have to be unset, because the fab build (which is executed below) calls
# git again, which will get confused if these variables are already set.
unset GIT_WORK_TREE
unset GIT_DIR

# Check out correct branch
git checkout $$BRANCH$$

# Update working tree to reflect new changes
git reset --hard

echo
