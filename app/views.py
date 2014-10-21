from flask import Blueprint, render_template

blueprint = Blueprint('main', __name__, template_folder='templates',
                      static_folder='static')

@blueprint.route('/')
def index():
    return render_template('main/index.html')
