"""
fabfile module that handles virtualenv-related tasks.
"""
from fabric.context_managers import settings, hide
from fabric.colors import cyan, red
from fabric.utils import abort
from fabfile.utils import do

venv_path = '.venv'
pip_cache_path = '.cache/pip'


def build():
    """Build or update the virtualenv."""
    with settings(hide('stdout')):
        print(cyan('\nUpdating venv, installing packages...'))
        do('[ -e %s ] || virtualenv %s --distribute --no-site-packages' % (venv_path, venv_path))
        do('mkdir -p %s' % pip_cache_path)
        # annoyingly, pip prints errors to stdout (instead of stderr), so we
        # have to check the return code and output only if there's an error.
        with settings(warn_only=True):
            pip = do('%s/bin/pip install --download-cache %s -r requirements.txt' % (venv_path, pip_cache_path), capture=True)
        if pip.failed:
            print(red(pip))
            abort("pip exited with return code %i" % pip.return_code)
