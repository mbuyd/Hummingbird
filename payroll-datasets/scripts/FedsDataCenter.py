import csv
from datetime import datetime
import json
import requests
from time import sleep

# url = "https://www.fedsdatacenter.com/federal-pay-rates/output.php?sColumns=,,,,,,,,&iDisplayStart=0&iDisplayLength=100"
url_prepend = "https://www.fedsdatacenter.com/federal-pay-rates/output.php?sColumns=,,,,,,,,&iDisplayStart="
url_append = "&iDisplayLength=100"

payload = {}
headers= {}

today = datetime.today()
date = str(today.year) + "-" + str(today.month) + \
    "-" + str(today.day) + "-" + str(today.hour) + str(today.minute)
table = open('FedsDataCenter-' + date + '.csv', 'w', newline='')
writer = csv.writer(table, delimiter=',')
writer.writerow(['name', 'grade', 'plan', 'salary', 'bonus', 'agency', 'location', 'occupation', 'fy'])

start = 384
end = 21083
pages = 21083

for i in range(start, end):
    print("Downloading page", i + 1, "of", pages,"..." ,end=" ")
    url = url_prepend + str(i * 100) + url_append
    response = requests.request("GET", url, headers=headers, data = payload)
    data = response.text.encode('utf8')
    parsed = json.loads(data)
    for item in parsed['aaData']:
        # print(item)
        writer.writerow(item)
    print("Done!")
    if (i + 1) % 1000 == 0:
        print("Sleeping for a half minute...")
        sleep(30)
        continue
    if (i + 1) % 100 == 0:
        print("Sleeping for a 5 seconds...")
        sleep(5)
        continue

# print(response.text.encode('utf8'))
