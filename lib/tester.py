import dataHandler

"""tests whether two different sets of values of a label are significantly different"""
"""data is the csv file, col is the column that we're grouping by (e.g. race), first is the
name of the first seperator (e.g. white) and second is the other (e.g. latino
or can be the whole data set)"""
def tester(data, col, first, second):
    "to do: parse data, set a variable = to those w/ first and those w/ second"
    data= parse(data)
    
