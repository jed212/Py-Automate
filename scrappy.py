
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

chromedriver_path = "/usr/bin/chromedriver"
chrome_service = webdriver.chrome.service.Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

products = []
brands = []
prices = []
categories = []

url = 'https://www.jumia.co.ke/catalog/?q=face+masks'
driver.get(url)

data = driver.page_source
soup = BeautifulSoup(data, features="html.parser")
articles = soup.findAll('article', attrs={'class':'prd _fb col c-prd'})

for article in articles:
    name = article.find('a', class_= 'core')['data-name']
    brand = article.find('a', class_= 'core')['data-brand']
    price = article.find('a', class_= 'core')['data-price']
    category = article.find('a', class_= 'core')['data-category']

    products.append(name)
    brands.append(brand)
    prices.append(price)
    categories.append(category)

df = pd.DataFrame({'Face Mask': products, 'Brand': brands, 'Price': prices, 'Category': categories})
df.to_csv('facemasks.csv', index=False, encoding='utf-8')
myFile = pd.read_csv('facemasks.csv')
print(myFile)