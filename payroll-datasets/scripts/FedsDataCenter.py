import csv
import requests
from time import sleep

# url = "https://www.fedsdatacenter.com/federal-pay-rates/output.php?sColumns=,,,,,,,,&iDisplayStart=0&iDisplayLength=100"
url_prepend = "https://www.fedsdatacenter.com/federal-pay-rates/output.php?sColumns=,,,,,,,,&iDisplayStart="
url_append = "&iDisplayLength=100"

payload = {}
headers= {}

# pages = 21083
pages = 3

for i in range(pages):
    print("Downloading page", i + 1, "of", pages,"..." ,end=" ")
    url = url_prepend + str(i) + url_append
    # response = requests.request("GET", url, headers=headers, data = payload)
    print("Done!")
    if (i + 1) % 1000 == 0:
        print("Sleeping for a minute...")
        sleep(5)
        continue
    if (i + 1) % 100 == 0:
        print("Sleeping for a half minute...")
        sleep(5)
        continue

# print(response.text.encode('utf8'))
