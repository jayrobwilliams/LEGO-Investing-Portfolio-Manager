import scraper
import csv
from collections import defaultdict

columns = defaultdict(list)
TAX_RATE = 1.10

with open("Brickfolio.csv", "r") as FILE:
    reader = csv.reader(FILE, delimiter=',')
    headers = next(reader)
    column_nums = range(len(headers))
    for row in reader:
        for i in column_nums:
            columns[headers[i]].append(row[i]) # row contains the info and i is the column number
    print(columns)

    for i, set_num in enumerate(columns['Set #']):
        url = "https://www.brickeconomy.com/search?query=" + str(set_num)
        set_info = scraper.get_values(url)
        columns['Current Val.'][i] = set_info['current value']
        columns['Retail Price'][i] = set_info['retail value'] #OPTIONAL if you want your retail values filled in
        print('...')

    with open("Brickfolio.csv", "w") as NEW_FILE:
        row_list = []

        writer = csv.writer(NEW_FILE)

        writer.writerow(headers)
        for i in range(len(columns[headers[0]])):
            for header in headers:
                row_list.append(columns[header][i])
            writer.writerow(row_list)
            row_list = []


