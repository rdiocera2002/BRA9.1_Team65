import urllib 
import requests

#Getting the public/external IP address using an API
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

#URL for the API that gets information from their external IP
url = "https://ipapi.co/" + external_ip + "/json"

#Getting the JSON data from the URL
json_data = requests.get(url).json()

#These are the labels that will be printed
labels = ["IP Address", "Version", "City", "Region", "Country", "ISP"]

#Keys that we will be getting from the JSON data
json_labels = ["ip", "version", "city", "region", "country_name", "org"]

#Printing the data
for i in range(len(labels)):
    print(labels[i] + ": " + json_data[json_labels[i]])