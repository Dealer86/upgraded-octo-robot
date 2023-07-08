import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("more_students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
