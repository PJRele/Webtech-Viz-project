# FROM CSV TO OBJECTS
# Cleo Boonstra
# 03/06/2019


import datetime as dt
import csv


# Get first name
def fname(any):
    try:
        nm = any.split(',')
        return nm[1]
    except IndexError:
        return ''


# Get last name
def lname(any):
    try:
        nm = any.split(',')
        return nm[0]
    except IndexError:
        return ''


# Convert string to integer or zero
def integer(any):
    return int(any or 0)


# Convert mm/dd/yyyy date to data or None
def date(any):
    try:
        return dt.datetime.strptime(any, "%m/%d/%Y").date()
    except ValueError:
        return None


# Convert any string to Boolean, FALSE if no value
def boolean(any):
    return bool(any)


# Convert string to float, or zero
def floatnum(any):
    s_balance = (any.replace('$', '').replace(',', '')).strip()
    return float(s_balance or 0)


# Create an empty list of people
people = []


# Define a class where each person is an object
class Person:
    def __init__(self, id, first_name, last_name, birth_year, date_joined, is_active, balance):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.date_joined = date_joined
        self.is_active = is_active
        self.balance = balance


# OPENING CSV FILE
# Open CSV file with UTF-8 encoding, don't read in newline characters.
with open('sample.csv', encoding='utf-8', newline='') as f:
    # Create a CSV row counter and row reader.
    reader = enumerate(csv.reader(f))

    # Skip the first row
    f.readline()

    # Loop through remaining rows one row at the time, i is counter, row is entire row.
    for i, row in reader:
        people.append(Person(i, fname(row[0]), lname(row[0]), integer(row[1]),
                             date(row[2]), boolean(row[3]), floatnum(row[4])))

# When above loop is done, show all objects in the people list
for p in people:
    print(p.id, p.first_name, p.last_name, p.birth_year, p.date_joined, p.is_active, p.balance)
