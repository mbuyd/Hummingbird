from flask import Blueprint, render_template, abort
from lib.dataHandler import *
dashboard = Blueprint('dashboard', __name__,
                        template_folder='templates')

@dashboard.route('/dashboard')
def show():
    return render_template('pages/dashboard.html',
        size = 500, 
        mfRatio = 99,
        meanTc = 5000000,
        jobCount = 5)

@dashboard.route('/dashboard/<filename>')
def filenameShow(filename):
    print(filename)
    print(parse(filename))
    
        
    return render_template('pages/dashboard.html',
        size = 500, 
        mfRatio = 99,
        meanTc = 5000000,
        jobCount = 5)