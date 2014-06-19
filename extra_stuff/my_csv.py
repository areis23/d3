import csv
with open('data.csv', 'wb') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(['Letter'] + ['Frequency'])
    datawriter.writerow(['A', 0.08167])