import Gender
Gender = Gender.Gender
import Job
Job = Job.Job
import Race
Race = Race.Race
import DataSections
DataSections = DataSections.DataSections
import disparitySearch
import dataHandler


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
    results[(Gender.MALE, Gender.FEMALE)] = dataHandler.search_disparity('sampledata.csv',  DataSections.GENDER, Gender.MALE.value, Gender.FEMALE.value)
    #race analysis
    for combination in generate_combinations(Race):
        results[combination] = dataHandler.search_disparity(datasetURL, DataSections.RACE, combination[0].value, combination[1].value )
    #job analysis
    for combination in generate_combinations(Job):
        results[combination] = dataHandler.search_disparity(datasetURL, DataSections.JOB, combination[0].value, combination[1].value )
    return results
