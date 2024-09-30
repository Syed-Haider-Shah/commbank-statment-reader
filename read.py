import csv
import re

pattern = r"(?=.*\bTransfer\b)"

with open('data.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  for line in csv_reader:
    if re.match(pattern, line[2]):
      print(line[2])