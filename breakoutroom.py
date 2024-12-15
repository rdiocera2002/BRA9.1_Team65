import urllib 
import requests

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

url = "https://ipapi.co/" + external_ip + "/json"
json_data = requests.get(url).json()


labels = ["IP Address", "Version", "City", "Region", "Country", "ISP"]
json_labels = ["ip", "version", "city", "region", "country_name", "org"]

for i in range(len(labels)):
    print(labels[i] + ": " + json_data[json_labels[i]])