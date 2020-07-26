import csv
import os

savefile = 'person.csv'
path = 'C:Users/rakes/OneDrive/Desktop/medilenz/code'

csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
with open('C:Users/rakes/OneDrive/Desktop/medilenz/code/person.csv', 'a+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)
csvFile.close() 