"""
fabfile module that handles deployment of the application to remote servers.
"""
import os
from fabric.api import env, local, run, put
from fabric.utils import abort
from fabric.colors import cyan, yellow
from fabric.contrib.console import confirm
from fabric.context_managers import settings, hide
from fabfile.servers import remote


def deploy(warn=True):
    """
    Deploy to remote environment.
    """
    with settings(host_string=remote()):

        if warn:
            # Display confirmation
            print('\nYou are about to deploy current branch ' + yellow('%(branch)s' % env, bold=True) + ' to ' + yellow('%(host_string)s' % env, bold=True) + '.')
            if not confirm('Continue?', default=False):
                abort('User aborted')

        # git-pull
        local('git pull origin %(branch)s' % env)

        # Initialise remote git repo
        run('git init %(remote_path)s' % env)
        run('git --git-dir=%(remote_path)s/.git config receive.denyCurrentBranch ignore' % env)
        local('cat %s/deployment/hooks/post-receive.tpl | sed \'s/\$\$BRANCH\$\$/%s/g\' > /tmp/post-receive.tmp' % (os.path.dirname(__file__), env.branch))
        put('/tmp/post-receive.tmp', '%(remote_path)s/.git/hooks/post-receive' % env)
        run('chmod +x %(remote_path)s/.git/hooks/post-receive' % env)

        # Add server to the local git repo config (as a git remote)
        with settings(hide('warnings'), warn_only=True):
            local('git remote rm %(branch)s' % env)
        local('git remote add %(branch)s ssh://%(user)s@%(host_string)s:%(port)s%(remote_path)s' % env)

        # Push to origin
        print(cyan('\nDeploying code...'))
        local('git push origin %(branch)s' % env)
        local('GIT_SSH=fabfile/deployment/ssh git push %(branch)s %(branch)s' % env)
