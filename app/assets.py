from os.path import join, abspath, dirname
from flask.ext.assetslite import Assets, Bundle
from flask.ext.assetslite.filters import cssmin, uglifyjs

# Static folder that all the paths below are relative from
static_folder = join(abspath(dirname(__file__)), 'static')

css = [
    'css/*.css',
]

js = [
    'js/vendor/rye-0.1.0.js',
]


def init(app):
    """
    Initialise assets on the app.
    """
    assets = Assets(app)
    assets.register('css', Bundle(css, output='__bundles/css/bundle.%s.css',
                                  filters=cssmin, static_folder=static_folder,
                                  cache_file='{0}/__bundles/css.cache'.format(static_folder)))

    assets.register('js', Bundle(js, output='__bundles/js/combined.%s.js',
                                  filters=uglifyjs, static_folder=static_folder,
                                  cache_file='{0}/__bundles/js.cache'.format(static_folder)))
    assets.build_all()

    return assets
