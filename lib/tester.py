import dataHandler


"""tests whether two different sets of values of a label are significantly different
    DATA - the csv file
    COL- the column/potential cause of discrimination being grouped (e.g. race)
    FIRST and SECOND - two cases of COL which are compared against each other ('asian' and 'white')
"""
def tester(data, col, first, second):
    #data= parse(data)
    data=[[2,0,3,1308697], [2,1,0,61831], [2,0,0,62847], [4,1,2,89537]]
    first= filter(col, 4, first)
    second= filter(col, 4, second)
    mfirst= mean(first)
    sfirst= sigma(first)
    msecond= mean(second)
    ssecond= sigma(second)
    denom= math.sqrt((sfirst**2/len(first))+(ssecond**2/len(second)))
    t_score= (mfirst-msecond)/(denom)
