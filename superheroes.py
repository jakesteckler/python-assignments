import json
import csv

#Read superheroes.json
with open('superheroes.json') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

print(rows)