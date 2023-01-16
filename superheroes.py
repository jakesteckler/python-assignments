import json
import csv

#Read superheroes.json
with open('superheroes.json') as f:
	superheroes = json.load(f)

#Write a header to CSV file
with open("superheroes.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(
        [
            "name",
            "age",
            "secretIdentity",
            "powers",
            "squadName",
            "homeTown",
            "formed",
            "secretBase",
            "active",
        ]
    )