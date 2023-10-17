# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class PostgresNoDuplicatesPipeline:
    def __init__(self):
        ## Connection Details
        hostname = 'localhost'
        username = 'jedidiah'
        password = '1234'
        database = 'reviews'

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS reviews(
            id serial PRIMARY KEY,
            asin VARCHAR(20),
            text TEXT,
            title TEXT,
            location_and_date VARCHAR(50), 
            verified BOOLEAN,
            rating NUMERIC(3, 2)
        )
        """)
        pass

    def process_item(self, item, spider):
        ## Check to see if text is already in database 
        self.cur.execute("select * from reviews where text = %s", (item['text'],))
        result = self.cur.fetchone()

        ## If it is in DB, create log message
        if result:
            spider.logger.warn("Item already in database: %s" % item['text'])

        ## if not in DB, insert data
        else:
            ## Define insert statement
            self.cur.execute(""" insert into reviews (asin, text, title, location_and_date, verified, rating) values (%s,%s,%s,%s,%s,%s)""", (
            item["asin"],
            item["text"],
            item["title"],
            item["location_and_date"],
            item["verified"],
            item["rating"]
        ))
            ## Execute insert of data into database
            self.connection.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database
        self.cur.close()
        self.connection.close()
        return item
