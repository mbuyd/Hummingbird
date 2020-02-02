from flask import Blueprint, render_template, abort
import os

manage = Blueprint('manage', __name__,
                        template_folder='templates')

@manage.route('/manage')
def show():
    files = os.listdir('uploads')
    return render_template('pages/manage.html', files = files)