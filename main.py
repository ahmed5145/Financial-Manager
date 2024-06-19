import csv
import gspread
import time
"""
gspread library allows us to configure and access google spread sheets through setting up google spread\
    sheets api
"""

month = 'may'
bank = 'hsbc'

file = f"{bank}_{month}.csv"

transactions = []

sum = 0
"""
Make sure that the file names of your csv sheets match the format above: bank_month.csv
or change the formatting of the file variable to match your needs.
"""
def manager(file):
    with open(file, mode= 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            #modify the following according to your csv file
            date = row[0]
            name = row[1]
            amount = float(row[2])
            sum += amount
            #category step is optional but you can clean up the sheet by categorizing the most 
            #frequent and known purchases
            category = 'other'
            if name == 'T-Mobile':
                category= 'phone_plan'
            transaction = ((date, name, amount, category))
            transactions.append(transaction)
        return transactions

#Make sure to setup google sheets service account and download the key(json file) as instructed.

sa = gspread.service_account()
sh = sa.open("Sheet_file_name")

wks = sh.worksheet(f"{month}")

rows = manager(file)

for row in rows:
    #customize according to your needs again
    wks.insert_row([row[0], row[1], row[2], row[3]], 8)
    time.sleep(2)
    