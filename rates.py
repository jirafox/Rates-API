import requests
from bs4 import BeautifulSoup

def get_exchange_rates():
    url = 'https://www.english.tgju.org'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Find the specific element containing the exchange rate
    rates = {}
    for rate in soup.find_all('table', class_='market-table'):  # Adjust the class name as needed
        currency = rate.find('span', class_='mini-flag').text  # Adjust the class name as needed
        value = rate.find('td', class_='nf')  # Adjust the class name as needed
        rates[currency] = value
    
    return rates
