import requests

print("Checking....")
#api to fetch ip adress
ip_add = requests.get('https://api.ipify.org').text
#finds geo location according to ip adress
url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
geo_q = requests.get(url)
geo_d = geo_q.json()
state = geo_d['city']
country = geo_d['country']
print(f"You Are Now In {state , country} .")
