import csv
import json
import math
import statistics
import sys

sys.path.append('lib')
import Gender
Gender = Gender.Gender
import Job
Job = Job.Job
import Race
Race = Race.Race
import DataSections
DataSections = DataSections.DataSections

def parse(file_name):
    data = []
    with open(file_name, 'r') as file:
        for row in csv.reader(file):
            data.append(row)
    return data[1:]

def splitCols(data):
    race = []
    gender = []
    job = []
    year = []
    salary = []
    for i in data:
        race.append(int(i[0]))
        gender.append(int(i[1]))
        job.append(int(i[2]))
        year.append(int(i[3]))
        salary.append(int(i[4]))
    return race, gender, job, year, salary


def singleFilter(labels, values, criteria):
    """
    singleFilter: filters a list based on the contents of another list

    Paramters:
     * labels: a list containing the objects you are searching for
     * values: a list containing the values you want to return at
               the index the label you are searching for is located
     * criteria: an object identical to the type stored in list that will
                 be compared to objects inside labels

    Description:
    The function iterates through labels, looking for matches to
    criteria, When a match is found, the item located at the same
    index in values is added to a new list, which is then returned
    after the entire list has been iterated through.
    """
    data = [x for x in values if criteria in labels]
    return data

def mean(lst):
    return sum(lst) / len(lst)

def meanOf(labels, values, criteria):
    data = singleFilter(labels, values, criteria)
    return sum(data) / len(data)

# Find standard deviation
def sigma(lst):
    return statistics.stdev(lst)

# Find standard deviation of criteria
def sigmaOf(labels, values, criteria):
    data = singleFilter(labels, values, criteria)
    return statistics.stdev(data)

# Returns the percentage of criteria in a list
def ratio(lst, criteria):
    data = [x for x in lst if x == criteria]
    return len(data) / len(lst)

def unique(lst):
    return list(dict.fromkeys(lst))

# Generate a dashboard summary
def dashSum(gender, job, salary):
    return len(gender), ratio(gender, Gender.MALE.value), math.floor(mean(salary)), len(unique(job))

def main():
    print("Begun handling of data with", sys.argv)
    argumentList = sys.argv[1:]
    data = parse(argumentList[0])

    # ['race', 'gender', 'job', 'year', 'salary']
    race, gender, job, year, salary = splitCols(data)
    # filter(gender, salary, Gender.FEMALE.value)
    count, ratio, meanTc, jobs = dashSum(gender, job, salary)

    dump = {
        "count": count,
        "ratio": ratio,
        "meanTc": meanTc,
        "jobs": jobs
    }
    with open('blobs/' + argumentList[0][7:-3] + ".json", 'w') as file:
        json.dump(dump, file)

#main()
