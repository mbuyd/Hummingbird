
import sys
sys.path.append("lib")
import dataHandler
import Gender
Gender = Gender.Gender
import Job
Job = Job.Job
import Race
Race = Race.Race
import DataSections
DataSections = DataSections.DataSections


"""tests whether two different sets of values of a label are significantly different, as determined by the salary column
    DATA - the csv file
    COL- the column/potential cause of discrimination being grouped (e.g. race)
    FIRST and SECOND - two cases of COL which are compared against each other ('asian' and 'white')
"""
def search_disparity(data, col, first, second):
    data = dataHandler.parse(data)
    data = dataHandler.splitCols(data)
    data1 = dataHandler.singleFilter(col, DataSections.SALARY, first)
    data2 = dataHandler.singleFilter(col, DataSections.SALARY, second)
    t_score_calc(data1, data2)

search_disparity("generated.txt", dataHandler.GENDER, Gender.MALE, Gender.FEMALE)
