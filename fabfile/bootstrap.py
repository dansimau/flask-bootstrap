"""
fabfile module for prepping a server for deploy.
"""
from fabric.colors import cyan
from fabric.context_managers import settings, hide
from fabfile.utils import do


def software():
    """
    Install required software.
    """
    with settings(remote_path='/tmp'):

        # Install prerequisites
        print(cyan('\nInstalling software...'))
        do('apt-get -qq update')
        do('apt-get -qq install -y puppet git')


def user():
    """
    Add and configure deploy user.
    """
    with settings(remote_path='/tmp'):

        # Set up deploy user
        print(cyan('\nSetting up deploy user...'))
        with settings(hide('warnings'), warn_only=True):
            do('useradd tobias')
        do('[ -e /home/tobias ] || cp -r /etc/skel /home/tobias')
        # Copy authorized_keys from the current user into deploy user's home
        do('mkdir -p /home/tobias/.ssh')
        do('[ -e ~/.ssh/authorized_keys ] && cp ~/.ssh/authorized_keys /home/tobias/.ssh/')
        do('chown -R tobias:tobias /home/tobias')


def project():
    """
    Set up project directory.
    """
    with settings(remote_path='/tmp'):
        # Set up project directory
        print(cyan('\nSetting up project directory...'))
        do('mkdir -p /srv/www/app')


def chown():
    """
    Fix project directory permissions after an initial deploy.
    """
    with settings(remote_path='/tmp'):
        print(cyan('\nFixing permissions...'))
        do('chown -R tobias:tobias /srv/www/app')
