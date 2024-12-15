from flask import Flask, render_template
import urllib 
import requests

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

url = "https://ipapi.co/" + external_ip + "/json"

json_data = requests.get(url).json()

ip = json_data['ip']
version = json_data['version']
city = json_data['city']
region = json_data['region']
country_name = json_data['country']
isp = json_data['org']

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html', html_ip = ip, html_version = version, html_city = city, html_region = region, html_country = country_name, html_isp = isp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)