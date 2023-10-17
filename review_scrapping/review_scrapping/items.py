# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ReviewScrappingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    asin = scrapy.Field()
    text = scrapy.Field()
    title = scrapy.Field()
    location_and_date = scrapy.Field()
    verified = scrapy.Field()
    rating = scrapy.Field()
    pass
