# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CardekhoScrapingItem(scrapy.Item):

    record_create_dt = scrapy.Field()
    feed_code = scrapy.Field()
    site = scrapy.Field()
    name = scrapy.Field()
    source_country = scrapy.Field()
    context_identifier = scrapy.Field()
    record_create_by = scrapy.Field()
    execution_id = scrapy.Field()
    specification = scrapy.Field()
    car = scrapy.Field()
    src = scrapy.Field()
