import csv
import random
from lib import Gender, Job, Race

"""
Generates a CSV file of sample size N.

input:
    N- the sample size
    Sample_instructions: a dictionary with instructions on how to bias people
    {
        key- the metric to be unfair about:
        value - a dictionary{
            key- the group in question:
            value- a number that indicates skew. eg 1.15 > 15% higher pay
        }
    }
    global_mean- a global average that is the relative comparison for all individual groups
    global_std- a global std for all.
"""
def generateCSV(sample_size, sample_instructions, global_mean, global_std):
    answer = list(sample_instructions) + ["wage"]
    for person in range(sample_size):
        person_attributes = []
        weighed_mean = global_mean
        for discriminating_factor in list(sample_instructions):
            factor_types = sample_instructions[discriminating_factor]
            selected_attribute = random.choice(list(factor_types))
            weighed_mean *=factor_types[selected_attribute]
            person_attributes += [selected_attribute]
        person_attributes += [int(100*random.gauss(weighed_mean, global_std))/100]
        answer.append(person_attributes)
    createCSV(answer)
    return answer

def createCSV(lists):
    with open('sampledata.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['race', 'gender', 'job', 'year', 'salary'])
        for row in lists:
            thewriter.writerow(row)

instruction = {
    'race' : {
        'white': 1.5,
        'black': 1,
        'asian': 1.3,
        'latino': 0.8,
        'indigenous': .8,
        'pacific': .9,
    },
    'gender' : {
        'male': 1,
        'female': 0.73,
    },
    'job' : {
        'Alcohol Beverage Purchasing Specialist': .5,
        'deputy sheriff': 1,
        'sheriff': 1.5,
        'Executive': 10
    }
}
for person in generateCSV(1500, instruction, 100000, 10000):
    print (person)
