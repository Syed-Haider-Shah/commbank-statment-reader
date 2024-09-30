import csv
import re

search_term = input("Please enter a search term: ")
pattern = fr"(?=.*{search_term})"

with open('data.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  for line in csv_reader:
    if re.match(pattern, line[2]):
      print(line[2])