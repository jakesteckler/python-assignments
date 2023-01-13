import csv
import json

#Read output/vegetables.csv (see previous section) into a variable called vegetables.
with open('output/vegetables.csv') as f:
	reader = csv.DictReader(f)
	vegetables = [row for row in reader]

#Print the variable vegetables.
print(vegetables)

#Write vegetables as a JSON file called output/vegetables.json. It should look like this:

with open('output/vegetables.json', 'w') as f:
    json.dump(vegetables, f)




