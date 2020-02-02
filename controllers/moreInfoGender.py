from flask import Blueprint, render_template, abort, request
from lib.dataHandler import *
moreInfoGender = Blueprint('moreInfoGender', __name__,
                        template_folder='templates')

@moreInfoGender.route('/moreInfoGender', methods=['GET','POST'])
def samplefunction():
    print(request.form)
        # permutations = data['data permutations']
    return render_template('pages/moreInfoGender.html') #, 
        #tVal = tValue,
        #dataPermutations = permutations)