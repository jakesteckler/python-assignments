import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#Loops through each vegetable
#In the loop, write the name of each vegetable and the color into a CSV called vegetables.csv
#Bonus: add the length of the name of the vegtable as separate column
with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "color", "length"])
    for vegetable in vegetables:
        writer.writerow([vegetable["name"], vegetable["color"], len(vegetable["name"])])



