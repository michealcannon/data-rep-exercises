# Write a program that stores the data for all trains in Ireland in a csv file


import requests
import csv
from bs4 import BeautifulSoup
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')
# print (soup.prettify())

listings = soup.findAll("objTrainPositions")
for listing in listings:
    print(listing)



