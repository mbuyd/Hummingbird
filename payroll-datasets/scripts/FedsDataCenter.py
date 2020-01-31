import requests
from time import sleep

# url = "https://www.fedsdatacenter.com/federal-pay-rates/output.php?sColumns=,,,,,,,,&iDisplayStart=0&iDisplayLength=100"
url_prepend = "https://www.fedsdatacenter.com/federal-pay-rates/output.php?sColumns=,,,,,,,,&iDisplayStart="
url_append = "&iDisplayLength=100"

payload = {}
headers= {}

pages = 21083

for i in range(21083):
    print("Downloading page", i + 1, "of", pages)
    url = url_prepend + str(i) + url_append
    # response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))
