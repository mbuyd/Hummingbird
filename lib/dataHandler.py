import csv
import json
import math
import statistics
import sys
import numpy as np

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
    data = []
    for i in range(len(labels)):
        if criteria == labels[i]:
            data.append(values[i])
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
    return len(gender), 100*ratio(gender, Gender.MALE.value), math.floor(mean(salary)), len(unique(job))

def pt_score_calc(data1, data2):
    c1 = (sigma(data1)**2)/len(data1)
    c2 = (sigma(data2)**2)/len(data2)
    m1 = mean(data1)
    m2 = mean(data2)
    denom= math.sqrt(c1+c2)
    tVal = (m1-m2)/denom
    return tVal

def search_disparity(data, col, first, second):
    data = parse(data)
    data = splitCols(data)
    data1 = singleFilter(data[col.value], data[DataSections.SALARY.value], first)
    if second > -1:
        data2 = singleFilter(data[col.value], data[DataSections.SALARY.value], second)
    else:
        data2 = data[DataSections.SALARY.value]
    return pt_score_calc(data1, data2)


"""Takes an interable and finds all possible, non duplicating possible pairs
returns: a list of tuples
"""
def generate_combinations(iterable):
    result = []
    avoid = []
    for iteration in iterable:
        for iteration2 in iterable:
            if iteration2 not in avoid and iteration2 is not iteration:
                result += [(iteration, iteration2)]
            avoid += [iteration]
    return result
def complete_data_analysis(datasetURL):
    results = {}
    #binary gender analysis
    results[(Gender.MALE, Gender.FEMALE)] = search_disparity('sampledata.csv',  DataSections.GENDER, Gender.MALE.value, Gender.FEMALE.value)
    #race analysis
    for combination in generate_combinations(Race):
        results[combination] = search_disparity(datasetURL, DataSections.RACE, combination[0].value, combination[1].value )
    #job analysis
    for combination in generate_combinations(Job):
        results[combination] = search_disparity(datasetURL, DataSections.JOB, combination[0].value, combination[1].value )
    return results


def main():
    print("Begun handling of data with", sys.argv)
    argumentList = sys.argv[1:]
    data = parse(argumentList[0])

    # ['race', 'gender', 'job', 'year', 'salary']
    race, gender, job, year, salary = splitCols(data)
    print(race)
    print(gender)
    print(job)
    print(year)
    print(salary)
    # filter(gender, salary, Gender.FEMALE.value)
    count, ratio, meanTc, jobs = dashSum(gender, job, salary)
    comprehensive_data_analysis = complete_data_analysis(argumentList[0])

    dump = {
        "count": count,
        "ratio": ratio,
        "meanTc": meanTc,
        "jobs": jobs,
        "t value": tVal,
        "data permutations": comprehensive_data_analysis,
        #"p value": pVal,
        }
    with open('blobs/' + argumentList[0][7:-3] + "json", 'w') as file:
        json.dump(dump, file)
        print("[dataHandler] saved!")

if len(sys.argv) > 1:
    main()
