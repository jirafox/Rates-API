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
        WebDriverWait(driver, 10).until(
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
    
    rates = {}
    for rate in soup.find_all("a", class_="data"):  # Adjust the class name as needed
        currency_element = rate.find("div", class_="title")  # Adjust the class name as needed
        value_element = rate.find("div", class_="buy")  # Adjust the class name as needed
        
        if currency_element and value_element:
            currency = currency_element.text.strip()
            value = value_element.text.strip()
            rates[currency] = value
    
    # Close the browser
    driver.quit()
    
    return rates

# Test the function
print(get_exchange_rates())
