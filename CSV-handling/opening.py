# CONVERTING
# Cleo Boonstra
# 03/06/2019
# Opening a CSV file and converting it to: strings, integers, data, boolean and floats

import csv
import datetime as dt

# Open CSV file with UTF-8 encoding, don't read in newline characters.
with open('sample.csv', encoding='utf-8', newline='') as f:
    # Create a CSV row counter and row reader.
    reader = enumerate(csv.reader(f))
    # Loop through one row at the time, i is counter, row is entire row.
    for i, row in reader:
        # Row 0 is heading, so ignore it.
        if i > 0:

            # CONVERTING TO STRINGS
            try:
                # full name split into two at comma.
                full_name = row[0].split(',')
                # Last name, strip extra space.
                last_name = full_name[0].strip()
                # First name, strip extra space
                first_name = full_name[1].strip()
            except IndexError:
                full_name = last_name = first_name = ""

            # CONVERTING TO INTEGERS
            # Birth year integer, zero for empty string.
            birth_year = int(row[1] or 0)

            # CONVERTING TO DATA
            # Data_joined is a date
            try:
                date_joined = dt.datetime.strptime(row[2], "%m/%d/%Y").date()
            except ValueError:
                date_joined = None

            # CONVERTING TO BOOLEAN
            # is_active is a Boolean, automatically False for empty string.
            is_active = bool(row[3])

            # CONVERTING TO FLOAT
            # Remove $, commas, leading and trailing spaces.
            str_balance = (row[4].replace('$', '').replace(',','')).strip()
            # Balance is a float or zero for a empty string.
            balance = float(str_balance or 0)

            # PRINT
            print(first_name, last_name, birth_year, date_joined, is_active, balance)
print('Done')