# Write a program that stores the data for all trains in Ireland in a csv file


import requests
import csv
from bs4 import BeautifulSoup
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')
# print (soup.prettify())

with open('week03_train.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    listings = soup.findAll("objTrainPositions")
    for listing in listings:
# print(listing)
        entryList = []
# print(listing.TrainLatitude.string)
# or
        entryList.append(print(listing.find('TrainLatitude').string))
        train_writer.writerow(entryList)

