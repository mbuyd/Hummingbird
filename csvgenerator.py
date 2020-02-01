import csv
import random

"""
Generates a CSV file of sample size N such that,
for each

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
    answer = []
    for person in range(sample_size):
        person_attributes = []
        weighed_mean = global_mean
        for discriminating_factor in list(sample_instructions):
            factor_types = sample_instructions[discriminating_factor]
            selected_attribute = random.choice(list(factor_types))
            weighed_mean *=factor_types[selected_attribute]
            person_attributes += [selected_attribute]
        person_attributes += [random.gauss(weighed_mean, global_std)]
        answer.append(person_attributes)
    return answer


instruction = {
    'race' : {
        'white': 1.5,
        'black': 0.8,
        'asian': 200,
        'indian': 0,
    },
    'gender' : {
        'male': 1.24,
        'female': 0.76,
    },
    'job' : {
        'bus operator': .5,
        'deputy sherriff': 1
    }
}
for person in generateCSV(40, instruction, 50000, 0.1):
    print (person)
