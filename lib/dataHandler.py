import csv
import statistics
import sys

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

def filter(labels, values, criteria):
    data = [x for x in values if criteria in labels]

def mean(lst):
    return sum(lst) / len(lst)

def meanOf(labels, values, criteria):
    data = [x for x in values if criteria in labels]
    return sum(data) / len(data)

# Find standard deviation
def sigma(lst):
    return statistics.stdev(lst)

# Find standard deviation of criteria
def sigmaOf(labels, values, criteria):
    data = [x for x in values if criteria in labels]


def main():
    argumentList = sys.argv[1:]
    data = parse(argumentList[0])

    # ['race', 'gender', 'job', 'year', 'salary']
    race, gender, job, year, salary = splitCols(data)

main()