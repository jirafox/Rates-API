from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def get_exchange_rates():
    url = 'https://alanchand.com/en/currencies-price'
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = "usr/bin/google-chrome"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get(url)
    
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "data"))
        )
    except Exception as e:
        print(f"Error waiting for elements: {e}")
        driver.quit()
        return {}
    
    page_source = driver.page_source
    
    soup = BeautifulSoup(page_source, 'html.parser')
    
    currency_rates = {}
    for rate in soup.find_all("a", class_="data"):
        currency_element = rate.find("div", class_="title")
        value_element = rate.find("div", class_="buy")
        
        if currency_element and value_element:
            currency = currency_element.text.strip()
            value = value_element.text.strip()
            currency_rates[currency] = value
    
    driver.quit()
    
    return currency_rates

def get_gold_rates():
    url = 'https://alanchand.com/en/gold-price'
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service('C:/Users/hassa/OneDrive/Documents/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(url)
        
        WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "body"))
        )
        
        page_source = driver.page_source
        
    except Exception as e:
        print(f"Error waiting for elements: {e}")
        return {}
    
    finally:
        driver.quit()
    
    soup = BeautifulSoup(page_source, 'html.parser')
    
    gold_rates = {}
    for rate in soup.find_all("div", class_="body"):
        title = rate.find("div", class_="title")
        persian = rate.find("div", class_="cell")
        if title and persian:
            gold_rates[title.get_text(strip=True)] = persian.get_text(strip=True)
    
    return gold_rates


def get_crypto_rates():
    url = 'https://alanchand.com/en/crypto-price'
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service('C:/Users/hassa/OneDrive/Documents/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(url)
        
        WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "body"))
        )
        
        page_source = driver.page_source
        
    except Exception as e:
        print(f"Error waiting for elements: {e}")
        return {}
    
    finally:
        driver.quit()
    
    soup = BeautifulSoup(page_source, 'html.parser')
    
    crypto_rates = {}
    for rate in soup.find_all("div", class_="body"):
        title = rate.find("div", class_="title")
        persian = title.find("div", class_="persian")
        other = rate.find("div", class_="other")
        price = other.find("div", class_="price")
        toman = price.find("div", class_="toman")
        
        if title and persian and toman:
            crypto_rates[persian.get_text(strip=True)] = toman.get_text(strip=True)
        else:
            print(f"Missing data in rate: {rate}")
    
    return crypto_rates
