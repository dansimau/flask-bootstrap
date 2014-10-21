"""
fabfile module containing Puppet-related tasks.
"""
from fabfile.utils import do
from fabric.colors import cyan
from fabric.context_managers import settings
from fabric.contrib.console import confirm
from fabric.decorators import task
from fabric.tasks import execute
from fabric.utils import abort

import servers


def check_syntax():
    """
    Syntax check on Puppet config.
    """
    print cyan('\nChecking puppet syntax...')
    do("find puppet -type f -name '*.pp' | xargs puppet parser validate")


@task
def remote(tag=None):
    """
    Run Puppet on remote servers.
    """
    if tag is None:
        if not confirm('Initiate Puppet run on all hosts?', default=False):
            abort('User aborted.')

    with settings(hosts=servers.remotes(tag=tag)):
        execute('code.deploy')
        execute('puppet.run')


@task
def run(debug=False):
    """
    Apply Puppet manifest.
    """
    check_syntax()

    print cyan('\nApplying puppet manifest...')
    if debug:
        debug = '--debug'
    else:
        debug = ''
    do('sudo /usr/bin/puppet apply puppet/manifests/default.pp '
       '--modulepath=puppet/modules {0}'.format(debug))
