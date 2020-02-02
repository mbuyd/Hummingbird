from flask import Blueprint, render_template, abort, request
from lib.dataHandler import *
dashboardItem = Blueprint('dashboardItem', __name__,
                        template_folder='templates')

@dashboardItem.route('/dashboardItem', methods=['GET','POST'])
def samplefunction():
    print(request.form['fileSub'])
    with open("blobs/"+request.form['fileSub']+".json") as json_file:
        data = json.load(json_file)
        print(data)
        num = data['count']
        ratio = '%.3f'%data['ratio']
        averageComp = data['meanTc']
        uniqueJobs = data['jobs']
    return render_template('pages/dashboardItem.html',
        size = num, 
        mfRatio = ratio,
        meanTc = averageComp,
        jobCount = uniqueJobs)