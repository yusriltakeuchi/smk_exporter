import csv
import requests
import json

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Script created by 
    Yusril Rapsanjani / @leeyurani
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

class SMK:
    def __init__(self, url):
        self.url = url

    #Get request to url
    def requestData(self):
        r = requests.get(self.url)
        return json.loads(r.text)

    #Get list of header for column
    def getHeaders(self, data):
        header = []
        for key in data[0].keys():
            header.append(key)
        return header

    #Exporting data to csv file
    def exportCSV(self, data, headers):
        #Try to converting to csv
        with open('smk_data.csv', mode="w", newline="") as csv_file:
            #Initialize
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            #Creating header
            writer.writeheader()
            
            #looping for every data founded
            for x in range(0, len(data)):
                #Writing data to csv
                writer.writerow(data[x])

#Data smk url
SMKURL = "https://portal.bandung.go.id/storage/json/smk.json"

#Initialize universitas Class
smk = SMK(SMKURL)
#Get data from server
data = smk.requestData()
#Get list of headers for column
headers = smk.getHeaders(data)
#Exporting data to csv
smk.exportCSV(data, headers)
