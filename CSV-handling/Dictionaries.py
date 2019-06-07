# IMPORTING CSV TO PYTHON DICTIONARIES
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


# Create an empty dictionary of people
people = {}

# OPENING CSV FILE
# Open CSV file with UTF-8 encoding, don't read in newline characters.
with open('sample.csv', encoding='utf-8', newline='') as f:
    # Create a CSV row counter and row reader.
    reader = enumerate(csv.reader(f))

    # Skip the first row
    f.readline()

    # Loop through remaining rows one row at the time, i is counter, row is entire row.
    for i, row in reader:
        newdict = dict({'first_name': fname(row[0]), 'last_name': lname(row[0]), 'birth_year': integer(row[1]), \
                        'date_joined': date(row[2]), 'is_active': boolean(row[3]), 'balance': floatnum(row[4])})
        people[i + 1] = newdict

# When above loop is done, show all objects in the people list
for person in people.keys():
    id = person
    print(id, people[person]['first_name'], \
          people[person]['last_name'], \
          people[person]['birth_year'], \
          people[person]['date_joined'], \
          people[person]['is_active'], \
          people[person]['balance'])
