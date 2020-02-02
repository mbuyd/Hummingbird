import dataHandler


"""tests whether two different sets of values of a label are significantly different"""
"""data is the csv file, col is the column that we're grouping by (e.g. race), first is the
name of the first seperator (e.g. white) and second is the other (e.g. latino
or can be the whole data set)"""
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
