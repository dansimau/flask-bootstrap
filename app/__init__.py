from os import listdir
from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
app.config.from_pyfile('%s/config/default.cfg' % app.root_path)
app.config.from_envvar('FLASK_CONFIG')

# Compile, combile and minify all static assets automatically
assets = Environment(app)
assets.register('js', Bundle(
    *['/'.join(['js', f]) for f in listdir('app/static/js')],
    filters='uglifyjs',
    output='assets/main.%(version)s.min.js'
))
assets.register('css', Bundle(
    # nested sass bundle
    Bundle(*['/'.join(['scss', f]) for f in listdir('app/static/scss')],
        filters='scss',
        output='assets/scss.combined.%(version)s.css'),
    # cssmin bundle
    *['/'.join(['css', f]) for f in listdir('app/static/css')],
    filters='cssmin',
    output='assets/combined.%(version)s.min.css'
))

@app.route('/')
def hello():
    return render_template('base.html')
