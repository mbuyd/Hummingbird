from flask import Blueprint, render_template, abort
from lib.dataHandler import *
dashboardItem = Blueprint('dashboardItem', __name__,
                        template_folder='templates')

"""@chicken.route('/chicken')
def show():
    return render_template('pages/chicken.html',
        size = 500, 
        mfRatio = 99,
        meanTc = 5000000,
        jobCount = 5)"""

