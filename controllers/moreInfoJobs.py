from flask import Blueprint, render_template, abort, request
from lib.dataHandler import *
moreInfoJobs = Blueprint('moreInfoJobs', __name__,
                        template_folder='templates')

@moreInfoJobs.route('/moreInfoJobs', methods=['GET','POST'])
def samplefunction():
    print(request.form)
        # permutations = data['data permutations']
    return render_template('/pages/moreInfoJobs.html') #, 
        #tVal = tValue,
        #dataPermutations = permutations)