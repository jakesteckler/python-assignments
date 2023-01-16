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

    #Loop over the members, and for each member write a row to the csv file
    for superhero in superheroes["members"]:
    	writer.writerow(
            [
                superhero["name"],
                superhero["age"],
                superhero["secretIdentity"],
                superhero["powers"],
                superheroes["squadName"],
                superheroes["homeTown"],
                superheroes["formed"],
                superheroes["secretBase"],
                superheroes["active"],
            ]
        )


