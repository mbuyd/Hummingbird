import csv
def parseCSV(file_name):
    
    with open(file_name, 'r') as file_o_data:
        csv_data = csv.reader(file_o_data)#gives an iterable
        processed_data = {'M':[],
        'F':[]} #gender:annual salary
        next(csv_data)
        for datapoint in csv_data:
            processed_data[datapoint[0]].append(datapoint[1])
        print("the average male pay is", sum([int(float(i)) for i in processed_data['M']])/len(processed_data['M']))
