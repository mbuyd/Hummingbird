import csv
def parseCSV(file_name):
    myList = []
    with open(file_name, 'r') as file_o_data:
        #csv_data = csv.reader(file_o_data)#gives an iterable

        for row in csv.reader(file_o_data):
            myList.append(row)
        print(myList)
        return myList
        processed_data = {'M':[],
        'F':[]} #gender:annual salary
        next(csv_data)
        for datapoint in csv_data:
            processed_data[datapoint[0]].append(datapoint[1])
        print("the average male pay is", sum([int(float(i)) for i in processed_data['M']])/len(processed_data['M']))

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

test_data = [['money', 'race'], [-100, 'white'], [25000, 'asian'], [26000, 'asian'], [1000000, 'egyptian'], [1000, 'white']]
sorted_test_data = sort_by(test_data, "money", "race")

"""
filter_group takes in a dataset and column to filter by (creating something like a "race-filter",
then takes in a name of the grouped variable (e.g. white))

filtergroup (test_data, race)(white)
>>> [[-100, 'white'], [1000, 'white']]
"""
filter_group = lambda dataset, col: lambda var: list(filter (lambda row: row[dataset[0].index(col)] == var, dataset))
print(filter_group(test_data, "race")("asian"))



def mean_data(sorted_data):
    return {grouper: (sum(values)/len(values)) for grouper, values in sorted_test_data.items() }
print(mean_data(test_data))






"""
Filters a CSV into several Lists, currently supported lists are categories, gender (index 0), annualSalary(index 1), Employee Title (index 2), and race (index 3)
"""
"""def filterCSV(file_name):
    with open(file_name, 'r') as file_o_data:
        csv_data = csv.reader(file_o_data) #gives an iterable
        categories = []
        gender = []
        annualSalary = []
        race = []
        employeeTitle = [] 
        #gender:annual salary

        for specData in next(csv_data):
            categories.append(specData)
        print(categories)

        for datapoint in csv_data:
            index = 0
            for specificData in datapoint:
                
                #print(specificData)
                categories = [category.lower() for category in categories]
                if ("gender" in categories and index == categories.index("gender")):
                    gender.append(specificData)
                elif ("current annual salary" in categories and index == categories.index("current annual salary")):
                    annualSalary.append(specificData)
                elif ("race" in categories and index == categories.index("race")):
                    race.append(specificData)
                if ("employee position title" in categories or "position title" in categories or "job" in categories):
                    if ("employee position title" in categories):
                        if (index == categories.index("employee position title")):
                            employeeTitle.append(specificData)
                    elif ("position title" in categories):
                        if (index == categories.index("position title")):
                            employeeTitle.append(specificData)
                    elif ("job" in categories):
                        if (index == categories.index("job")):
                            employeeTitle.append(specificData)
                    
                #elif (index == categories.index("Employee Position Title") or index == categories.index("Position Title")):
                #    employeeTitle.append(specificData)
                index += 1
        return [gender, annualSalary, employeeTitle, race]"""

#gender = 'M' or 'F'
def genderSalaryAVG(arr, seekGender):
    
    gender = arr[0]
    annualSalary = arr[1]

    if ((seekGender != 'M' and seekGender != 'F') or gender == []):
        return

    totalAnn = 0
    index = 0
    count = 0

    for data in gender:
        if (data.lower() == seekGender.lower() and annualSalary[index] != ''):

            totalAnn += float(annualSalary[index])
            count += 1
        index += 1

    print("Average annual salary for gender: "+seekGender+", is "+(str(int(totalAnn/count))))

    return (str(int(totalAnn/count)))

def raceAVG(arr, seekRace):
    
    race = arr[3]
    annualSalary = arr[1]
    if (seekRace == [] or race == [] or annualSalary == []):
        return
    totalAnn = 0
    index = 0
    count = 0

    for data in race:
        if (data.lower() == seekRace.lower() and annualSalary[index] != ''):

            totalAnn += float(annualSalary[index])
            count += 1
        index += 1

    print("Average annual salary for race: "+seekRace+", is "+(str(int(totalAnn/count))))

    return (str(int(totalAnn/count)))
    