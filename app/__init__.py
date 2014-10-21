import os
from os.path import abspath, relpath
from flask import Flask, request_finished, render_template

import assets
import jinja
import logger
import views

def create_app(config=None):
    """
    Create and initialise the application.
    """
    app = Flask(__name__)
    app.config.from_pyfile('%s/config/default.py' % app.root_path)

    if config:
        app.config.from_pyfile(config)
    elif os.getenv('FLASK_CONFIG'):
        app.config.from_envvar('FLASK_CONFIG')

    logger.init(app)
    jinja.init(app)
    assets.init(app)

    app.register_blueprint(views.blueprint)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(500)
    def server_error(error):
        return render_template('errors/default.html'), 500

    return app
