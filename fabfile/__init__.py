from fabric.decorators import task

import app
import db
import puppet
import virtualenv

@task
def build():
    """Execute build tasks for all components."""
    virtualenv.build()
    db.build()

@task
def run():
    """Start app in debug mode (for development)."""
    app.run()