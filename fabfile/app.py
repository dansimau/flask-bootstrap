from fabric.decorators import task
from fabric.context_managers import settings
from utils import do

@task
def run():
    """Start app in debug mode (for development)."""
    do('export FLASK_CONFIG=$PWD/app/config/dev.cfg && venv/bin/python ./run.py')
