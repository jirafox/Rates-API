from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_exchange_rates():
    url = 'https://alanchand.com/en/currencies-price'
    
    # Set up Selenium with ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service('C:/Users/hassa/OneDrive/Documents/chromedriver.exe')  # Update with your ChromeDriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Load the webpage
    driver.get(url)
    
    # Wait for the elements to be present
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "data"))
        )
    except Exception as e:
        print(f"Error waiting for elements: {e}")
        driver.quit()
        return {}
    
    # Get the page source after JavaScript has rendered
    page_source = driver.page_source
    
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    currency_rates = {}
    for rate in soup.find_all("a", class_="data"):  # Adjust the class name as needed
        currency_element = rate.find("div", class_="title")  # Adjust the class name as needed
        value_element = rate.find("div", class_="buy")  # Adjust the class name as needed
        
        if currency_element and value_element:
            currency = currency_element.text.strip()
            value = value_element.text.strip()
            currency_rates[currency] = value
    
    # Close the browser
    driver.quit()
    
    return currency_rates

def get_gold_rates():
    url = 'https://alanchand.com/en/gold-price'
    
    # Set up Selenium with ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service('C:/Users/hassa/OneDrive/Documents/chromedriver.exe')  # Update with your ChromeDriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Load the webpage
        driver.get(url)
        
        # Wait for the elements to be present
        WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "body"))
        )
        
        # Get the page source after JavaScript has rendered
        page_source = driver.page_source
        
    except Exception as e:
        print(f"Error waiting for elements: {e}")
        return {}
    
    finally:
        # Close the browser
        driver.quit()
    
    # Parse the page source with BeautifulSoup
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
    
    # Set up Selenium with ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service('C:/Users/hassa/OneDrive/Documents/chromedriver.exe')  # Update with your ChromeDriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Load the webpage
        driver.get(url)
        
        # Wait for the elements to be present
        WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "body"))
        )
        
        # Get the page source after JavaScript has rendered
        page_source = driver.page_source
        
    except Exception as e:
        print(f"Error waiting for elements: {e}")
        return {}
    
    finally:
        # Close the browser
        driver.quit()
    
    # Parse the page source with BeautifulSoup
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

# Example usage
print(get_crypto_rates())

# Example usage
print(get_gold_rates())

# Test the function
print(get_exchange_rates())
