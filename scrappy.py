
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/bin/chromedriver")

products = []
ratings = []
prices = []

url = 'https://www.jumia.co.ke/nourishing-cocoa-body-lotion-with-cocoa-butter-400ml-pack-of-2-nivea-mpg434442.html'
driver.get(url)

data = driver.page_source
soup = BeautifulSoup(data)

for a in soup.findAll('a', href=True, attr ={}):