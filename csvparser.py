import csv
def parseCSV(file_name):

    with open(file_name, 'r') as file_o_data:
        csv_data = csv.reader(file_o_data)#gives an iterable
        return csv_data

"""csv's will have a standard of gender in col 0, salary in col 4
if csv is homemade, race, then job"""


"""
Takes DATA, an iterable, and sorts the DATA by the
COLUMN_SORT and returns it as a dictionary where each different type
in COLUMN_GROUP has its relevant COLUMN_SORTs listed as a dictionary value.
"""
def sort_by(data, column_sort, column_group ):
    assert len(data)>1, "There is no data in the file!"
    header, data = data[0], data[1:]
    try:
        group_ind = header.index(column_group)
        sort_ind = header.index(column_sort)
    except ValueError:
        return "Error: the request is not represented by the data"
    sorted_data = {}
    for data_point in data:
        grouper = data_point[group_ind]
        sort_value = data_point[sort_ind]
        if grouper not in sorted_data:
            sorted_data[grouper] = [sort_value]
        else:
            sorted_data[grouper] += [sort_value]
    return sorted_data



#test_data = [['money', 'race'], [-100, 'white'], [25000, 'asian'], [26000, 'asian'], [1000000, 'egyptian'], [1000, 'white']]
#sorted_test_data = sort_by([['money', 'gender'], [-100, 'male'], [25000, 'female'], [26000, 'male'], [1000000, 'male'], [1000, 'female']], "money", "race")
#print(sorted_test_data)

gender_test = [['gender','race','job', 'salary'], ['male','a','aa', 10], ['female','a','ab', 11], ['male','a','ab', 12], ['female','a','aa', 12]]


"""takes in a parsed csv that has gender in col 0, salary in col 3 """
def test_genders(data):
    assert len(data)>1, "There is no data in the file!"
    header, data = data[0], data[1:]
    sorted_data={'male': [], 'female': []}
    for data_point in data:
        if(data_point[0]=='male'):
            sorted_data.get('male').append((data_point))
        else:
            sorted_data.get('female').append((data_point))
    print(sorted_data)

test_genders(gender_test)

"""
filter_group takes in a dataset and column to filter by (creating something like a "race-filter",
then takes in a name of the grouped variable (e.g. white))

filtergroup (test_data, race)(white)
>>> [[-100, 'white'], [1000, 'white']]
"""
filter_group = lambda dataset, col: lambda var: list(filter (lambda row: row[dataset[0].index(col)] == var, dataset))
#print(filter_group(test_data, "race")("asian"))



def mean_data(sorted_data):
    return {grouper: (sum(values)/len(values)) for grouper, values in sorted_test_data.items() }
#print(mean_data(test_data))
