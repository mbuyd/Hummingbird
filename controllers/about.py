from flask import Blueprint, render_template, abort

about = Blueprint('about', __name__,
                        template_folder='templates')

@about.route('/about')
def show():
    return render_template('pages/placeholder.about.html')