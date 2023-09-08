# import the required libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Set up Chrome WebDriver options for headless browsing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

chromedriver_path = "/usr/bin/chromedriver"

"""
Create a webdriver service and initialize the
Chrome WebDriver with the service and options
"""
chrome_service = webdriver.chrome.service.Service(
    executable_path=chromedriver_path
    )
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

products = []
brands = []
prices = []
categories = []

url = 'https://www.jumia.co.ke/catalog/?q=face+masks'
driver.get(url)

# Get a page source html and create a beautifulsoup object to parse the html
data = driver.page_source
soup = BeautifulSoup(data, features="html.parser")
articles = soup.findAll('article', attrs={'class': 'prd _fb col c-prd'})

# Extract the name, brand, price, and category from each article
for article in articles:
    name = article.find('a', class_='core')['data-name']
    brand = article.find('a', class_='core')['data-brand']
    price = article.find('a', class_='core')['data-price']
    category = article.find('a', class_='core')['data-category']

    products.append(name)
    brands.append(brand)
    prices.append(price)
    categories.append(category)

df = pd.DataFrame(
    {
        'Face Mask': products,
        'Brand': brands,
        'Price': prices,
        'Category': categories
    }
    )
# dataframe to json file
df.to_json('output.json', orient='records', lines=True)

# dataframe to csv file
df.to_csv('facemasks.csv', index=False, encoding='utf-8')

myFile = pd.read_csv('facemasks.csv')
