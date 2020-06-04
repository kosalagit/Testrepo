import requests
result=requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=mf0Jn2yR620g9bCu5FQjQsQ76Zfa4GnhG9ZbCTrs')
result.statusCode
result.text
result.json
