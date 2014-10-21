"""
fabfile module containing application-specific tasks.
"""
from fabric.api import task
from fabric.colors import cyan
from fabfile.utils import do
from fabfile.virtualenv import venv_path


@task
def build():
    """
    Run application build tasks.
    """
    # Generate static assets. Note that we always build assets with the
    # production config because dev will never point to compiled files.
    print(cyan('\nBuilding static assets...'))
    do('mkdir -p app/static/__bundles/css')
    do('mkdir -p app/static/__bundles/js')
    do('export FLASK_CONFIG=config/production.py && %s/bin/python manage.py build' % venv_path)


def run():
    """Start app in debug mode (for development)."""
    do('export FLASK_CONFIG=config/dev.py && %s/bin/python manage.py runserver' % venv_path)


def test():
    """Run unit tests"""
    print(cyan('\nRunning tests...'))
    do('FLASK_CONFIG=config/test.py %s/bin/nosetests --exclude-dir-file=\'.noseexclude\' --with-yanc --with-spec --spec-color -q' % venv_path)


def coverage():
    """Generate test coverage report"""
    do('FLASK_CONFIG=config/test.py %s/bin/nosetests --exclude-dir-file=\'.noseexclude\' --with-cov --cov=app --cov-report=html' % venv_path)


def start():
    """Start app using init."""
    do('sudo start uwsgi')


def stop():
    """Stop app using init."""
    do('sudo stop uwsgi')


def reload():
    """Restart app using init."""
    do('sudo reload uwsgi')
