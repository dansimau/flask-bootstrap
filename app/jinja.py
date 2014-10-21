from flask import request


def init(app):
    @app.context_processor
    def debug(debug=app.debug):
        """
        Notify templates that they're in debug mode
        """
        return dict(debug=debug)

    @app.context_processor
    def request_global():
        """
        Make request available in templates
        """
        return dict(request=request)
