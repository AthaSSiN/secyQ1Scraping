import csv
import json
import re

regex = "^[a-z]*([A-Z][a-zA-Z]*[\s]|[\s][a-z\s]*[A-Z])[a-zA-Z\s]*$"

# seperates out single word names / names with special symbols / names with no capital letters 

valid = []

with open('result.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            x = re.search(regex, row[0])
            if(x != None):
                valid.append([row[0], row[1], row[2]])
            else:
                print(f'{row[0]} is an invalid name')
        line_count += 1
    print(f'\nProcessed {line_count} lines.')

valid.sort()
print(f"Number of Valid Names : {len(valid)} \n")

file = open('students.json')
data = json.load(file)

for i in valid:
    for person in data:
        jsonName = person['n'].lower().split()
        gsocName = i[0].lower().split()
        if jsonName == gsocName:
            print(f"Name : {i[0]}, Roll No : {person['i']},  Branch : {person['d']}, Organisation : {i[1]}, Project : {i[2]} \n")