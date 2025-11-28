import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = requests.get(url)
print(response)
data = response.json()
print(data)
# {'table': 'A',
# 'currency': 'euro',
# 'code': 'EUR',
# 'rates': [{'no': '231/A/NBP/2025', 'effectiveDate': '2025-11-28', 'mid': 4.2369}]}

