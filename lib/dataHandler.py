import csv
import json
import statistics
import sys

from . import Gender
Gender = Gender.Gender

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
        race.append(i[0])
        gender.append(i[1])
        job.append(i[2])
        year.append(i[3])
        salary.append(i[4])
    return race, gender, job, year, salary

"""
filters VALUES for VALUES where CRITERIA
"""
def filter_jank(labels, values, criteria):
    data = [x for x in values if criteria in labels]
    return data

def mean(lst):
    return sum(lst) / len(lst)

def meanOf(labels, values, criteria):
    data = filter_jank(labels, values, criteria)
    return sum(data) / len(data)

# Find standard deviation
def sigma(lst):
    return statistics.stdev(lst)

# Find standard deviation of criteria
def sigmaOf(labels, values, criteria):
    data = filter(labels, values, criteria)
    return statistics.stdev(data)

# Returns the percentage of criteria in a list
def ratio(list, criteria):
    data = [x for x in list if x == criteria]
    return len(data) / len(list)

def unique(lst):
    return list(dict.fromkeys(lst))

# Generate a dashboard summary
def dashSum(gender, job, salary):
    return len(gender), ratio(gender, Gender.MALE), mean(salary), len(unique(job))

def main():
    argumentList = sys.argv[1:]
    data = parse(argumentList[0])

    # ['race', 'gender', 'job', 'year', 'salary']
    race, gender, job, year, salary = splitCols(data)
    count, ratio, meanTc, jobs = dashSum(gender, job, salary)

    dump = {
        "count": count,
        "ratio": ratio,
        "meanTc": meanTc,
        "jobs": jobs
    }
    with open('blobs/' + argumentList[0][7:-3] + ".json", 'w') as file:
        json.dump(dump, file)

main()
