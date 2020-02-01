import csv
def parseCSV(file_name):
    with open(file_name, 'r') as file_o_data:
        csv_data = csv.reader(file_o_data)#gives an iterable
        for i in range(50):
            print(next(csv_data))
