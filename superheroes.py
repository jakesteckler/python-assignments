import json
import csv

#Read superheroes.json
with open('superheroes.json') as f:
	superheroes = json.load(f)
