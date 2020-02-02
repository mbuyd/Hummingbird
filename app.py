#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, Blueprint, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os
import sys
import webbrowser


from lib import *
from controllers import *
import parser

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

MIN_PYTHON = (3, 5)

def versionCheck():
    if sys.version_info < MIN_PYTHON:
        sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

def create_app():
    return Flask(__name__);

app = create_app();

app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


app.register_blueprint(home.home)
app.register_blueprint(upload.upload)
app.register_blueprint(success.success)
app.register_blueprint(dashboard.dashboard)
app.register_blueprint(manage.manage)

@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)

@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.

@app.route('/', methods=['GET', 'POST'])
def searchHome():
    search = request.form
    
    if request.method == 'POST':
        print("SHOULD SEARCH: "+search.get('search'))
        url = "http://www.google.com/search?q="+search.get('search')
        webbrowser.open_new_tab(url)
        return render_template('pages/home.html')
    #return render_template('pages/upload.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def searchDashboard():
    search = request.form
    
    if request.method == 'POST':
        print("SHOULD SEARCH: "+search.get('search'))
        url = "http://www.google.com/search?q="+search.get('search')
        webbrowser.open_new_tab(url)
        return render_template('pages/dashboard.html',
        size = 500, 
        mfRatio = 99,
        meanTc = 5000000,
        jobCount = 5)

@app.route('/manage', methods=['GET', 'POST'])
def searchManage():
    search = request.form
    if request.method == 'POST':
        print("SHOULD SEARCH: "+search.get('search'))
        url = "http://www.google.com/search?q="+search.get('search')
        files = os.listdir('uploads')
        webbrowser.open_new_tab(url)
        return render_template('pages/manage.html', files = files)

@app.route('/upload', methods=['GET', 'POST'])
def searchUpload():
    search = request.form
    
    if request.method == 'POST':
        print("SHOULD SEARCH: "+search.get('search'))
        url = "http://www.google.com/search?q="+search.get('search')
        webbrowser.open_new_tab(url)
        return render_template('pages/upload.html')

@app.route('/search', methods=['GET', 'POST'])
def searchSuccess():
    search = request.form
    
    if request.method == 'POST':
        print("SHOULD SEARCH: "+search.get('search'))
        url = "http://www.google.com/search?q="+search.get('search')
        webbrowser.open_new_tab(url)
        return render_template('pages/home.html')


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
