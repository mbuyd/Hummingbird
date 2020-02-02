
import sys
sys.path.append("lib")
from dataHandler import parse, splitCols, singleFilter, pt_score_calc
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


# search_disparity("sampledata.csv", DataSections.GENDER, Gender.MALE.value, Gender.FEMALE.value)
