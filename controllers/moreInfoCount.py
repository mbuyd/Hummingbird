from flask import Blueprint, render_template, abort, request
from lib.dataHandler import *
moreInfoCount = Blueprint('moreInfoCount', __name__,
                        template_folder='templates')

@moreInfoCount.route('/moreInfoCount', methods=['GET','POST'])
def samplefunction():
    print(request.form)
        # permutations = data['data permutations']
    return render_template('pages/moreInfoCount.html') #, 
        #tVal = tValue,
        #dataPermutations = permutations)