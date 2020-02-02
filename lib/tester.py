
import sys
sys.path.append("lib")
import dataHandler
import Gender
import Job
import Race


"""tests whether two different sets of values of a label are significantly different, as determined by the salary column
    DATA - the csv file
    COL- the column/potential cause of discrimination being grouped (e.g. race)
    FIRST and SECOND - two cases of COL which are compared against each other ('asian' and 'white')
"""
def tester(data, col, first, second):
    data= parse(data)
    data= splitCols(data)
    first= filter(col, 4, first)
    second= filter(col, 4, second)
    mfirst= mean(first)
    sfirst= sigma(first)
    msecond= mean(second)
    ssecond= sigma(second)
    denom= math.sqrt((sfirst**2/len(first))+(ssecond**2/len(second)))
    t_score= (mfirst-msecond)/(denom)

tester("generated.txt", 0, 0, 1)
