import requests
import json


r1 = requests.get("http://astral.hacksoft.io/api/airline/?format=json")
r2 = requests.get("http://data.okfn.org/data/core/country-list/r/data.json")
r1_json = r1.json()
r2_json = r2.json()

histogram = {}
count = 0
for airline in r1_json:
    for country in r2_json:
        if airline["country_code"] == country["Code"]:
            if country["Name"] in histogram:
                histogram[country["Name"]] += 1

            else:
                histogram[country["Name"]] = 1


with open('country_histogram.json', 'w') as f:
    json.dump(histogram, f, ensure_ascii=False, indent=4)
