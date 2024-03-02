import csv
with open('/Users/prenses/Documents/PythonProjectsAndHomeworks/csv_denemeleri/eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))