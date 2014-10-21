from fabric.api import env
from fabric.utils import abort
from fabric.decorators import task
from fabric.context_managers import settings

# Load configuration
import config

# Fabfile modules
import app
import db
import bootstrap as _bootstrap
import deployment as code
import puppet
import servers
import virtualenv


@task
def bootstrap():
    """
    Set up a new server (requires superuser credentials).
    """
    # Very important that we only do this on remote machines and not locally.
    if not env.host_string:
        abort('You must specify a server to configure using -H.')

    # Use sudo if we're not logging on as root
    if env.user != 'root':
        env.sudo = True

    # Bootstrap stuff
    _bootstrap.software()
    _bootstrap.user()
    _bootstrap.project()

    # Initial code deploy
    code.deploy(warn=False)

    # Initial puppet run
    puppet.run()

    # Fix permissions
    _bootstrap.chown()

    # Ready to deploy now


@task
def build():
    """
    Execute build tasks.
    """
    virtualenv.build()
    app.build()
    db.build()


@task
def run():
    """
    Run app in debug mode (for development).
    """
    app.run()


@task
def test():
    """Run tests."""
    app.test()


@task
def deploy():
    """
    Deploy to remote environment.

    Deploys code from the current git branch to the remote server and reloads
    services so that the new code is in effect.

    The remote server to deploy to is automatically determined based on the
    currently checked-out git branch and matched to the configuration specified
    in fabfile/deploy/config.py.
    """
    code.deploy()
    # Post-deploy tasks on the remote server
    with settings(host_string=servers.remote()):
        build()
        puppet.run()
        app.reload()
