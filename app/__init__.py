from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('%s/config/default.cfg' % app.root_path)
app.config.from_envvar('FLASK_CONFIG')

@app.route('/')
def hello():
    return render_template('base.html')
