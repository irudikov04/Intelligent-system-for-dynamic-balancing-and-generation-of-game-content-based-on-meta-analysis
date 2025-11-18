import requests  
url = 'https://api.opendota.com/api/matches/5905070268'  
response = requests.get(url)  
data = response.json()  
print(data)  
