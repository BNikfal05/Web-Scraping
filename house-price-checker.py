from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

#Constant, not changing, environment
URL = "https://appbrewery.github.io/Zillow-Clone"


def clean_up_price(price_html_tag:str) -> str:
    formated_price = price_html_tag.getText()
    for idx, char in enumerate(formated_price):
        print(formated_price)
        print(idx)
        try:
            int(formated_price[idx])
        except ValueError:
            if idx == 0 or formated_price[idx] == "," or formated_price[idx] == ".":
                pass
            formated_price = formated_price.split(char[idx])[0]
        else:
            pass
    return formated_price

# Setting up Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


# Setting up BeautifulSoup
website = requests.get(URL).text
soup = BeautifulSoup(website, "html.parser")
house_price_tags = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
house_address_tags = soup.find_all(name="address")
houses_URL_tags = soup.find_all(name="a", class_="property-card-link", href=True)
house_prices = [clean_up_price(price) for price in house_price_tags]
house_addresses = [address.getText().strip() for address in house_address_tags]
house_URLs = [url['href'] for url in houses_URL_tags]
print(house_prices)
#print(house_addresses)
#print(house_URLs)