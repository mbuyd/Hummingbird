from flask import Blueprint, render_template, abort

upload = Blueprint('upload', __name__,
                        template_folder='templates')

@upload.route('/upload')
def show():
    return render_template('pages/upload.html')