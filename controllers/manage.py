from flask import Blueprint, render_template, abort

manage = Blueprint('manage', __name__,
                        template_folder='templates')

@manage.route('/manage')
def show():
    return render_template('pages/manage.html')