# Project 2: Covid Data Analysis using .csv file

import csv
import copy
import random

template = {
   "date": "",
   "new_cases": 0,
   "deaths": 0,
   "recovered": 0
}

data = []

with open('Day5\covid.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        day_data = copy.deepcopy(template)
        day_data["date"] = row[0]
        day_data["new_cases"] = int(row[1])       
        day_data["deaths"] = int(row[2])
        day_data["recovered"] = int(row[3])
        data.append(day_data)
#print(data)

#total_cases = sum(day["new_cases"] for day in data)

total_cases = 0

for day in data:
    total_cases += day["new_cases"]

print(total_cases)

total_deaths = sum(day["deaths"] for day in data)
print(total_deaths)

total_recovered = sum(day["recovered"] for day in data)
print(total_recovered)

average = total_cases / len(data)

random_day = random.choice(data)
print(random_day['date'])
print(random_day['recovered'])