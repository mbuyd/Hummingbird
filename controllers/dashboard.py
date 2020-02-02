from flask import Blueprint, render_template, abort
from lib.dataHandler import *
dashboard = Blueprint('dashboard', __name__,
                        template_folder='templates')

@dashboard.route('/dashboard')
def show():
    return render_template('pages/dashboard.html',
        size = 4123, 
        mfRatio = 51,
        meanTc = 251222,
        jobCount = 5)

