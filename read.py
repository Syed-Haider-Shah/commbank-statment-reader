import csv
import re

search_term_1 = input("Month ")
search_term_2 = input("Search ")
pattern1 = fr"(?=.*{search_term_1})"
pattern2 = fr"(?=.*{search_term_2})"

with open('data2.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  for line in csv_reader:
    if re.match(pattern1, line[0]):
      if re.match(pattern2, line[2]):
        print(line[2], line[1])