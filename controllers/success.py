from flask import Blueprint, render_template, abort, request
import csvparser
success = Blueprint('success', __name__,
                        template_folder='templates')

@success.route('/success', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save('uploads/' + f.filename)
      csvparser.parseCSV('uploads/' + f.filename)
      return render_template('forms/success.html', name = f.filename)
