from flask import Blueprint, render_template, abort, request
from lib.dataHandler import *
moreInfoSalary = Blueprint('moreInfoSalary', __name__,
                        template_folder='templates')

@moreInfoSalary.route('/moreInfoSalary', methods=['GET','POST'])
def samplefunction():
    print(request.form)
        # permutations = data['data permutations']
    return render_template('pages/moreInfoSalary.html') #, 
        #tVal = tValue,
        #dataPermutations = permutations)