
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

chromedriver_path = "/usr/bin/chromedriver"
chrome_service = webdriver.chrome.service.Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

products = []
ratings = []
prices = []

url = 'https://www.jumia.co.ke/catalog/?q=face+masks'
driver.get(url)

data = driver.page_source
soup = BeautifulSoup(data, features="html.parser")

# for a in soup.findAll('a', href=True, attr ={}):