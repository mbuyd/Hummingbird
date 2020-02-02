from flask import Blueprint, render_template, abort, request
from lib.dataHandler import *
dashboardItem = Blueprint('dashboardItem', __name__,
                        template_folder='templates')

@dashboardItem.route('/dashboardItem', methods=['GET','POST'])
def samplefunction():
    if (request.method == 'POST'):
        print(request.form['fileSub'])
        with open("blobs/"+request.form['fileSub']+".json") as json_file:
            data = json.load(json_file)
            print(data)
            num = data['count']
            ratio = '%.3f'%data['ratio']
            averageComp = data['meanTc']
            uniqueJobs = data['jobs']
            gend = int(data['p_val_g']*1000)/1000
            rac = int(data['p_val_race']*1000)/1000
            # tValue = data['t value']
            # permutations = data['data permutations']
        return render_template('pages/dashboardItem.html',
            size = num,
            mfRatio = ratio,
            meanTc = averageComp,
            jobCount = uniqueJobs,
            p_val_g = gend,
            p_val_race = rac)
            #tVal = tValue,
            #dataPermutations = permutations)
    else:
        return render_template('pages/dashboardItem.html')
