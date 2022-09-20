import scrapy


class CardekhoItem(scrapy.Item):

    car_title = scrapy.Field()
    price_blurb = scrapy.Field()
    fuel_type = scrapy.Field()
    gear_box = scrapy.Field()
    variant = scrapy.Field()
    mileage = scrapy.Field()
    record_create_date = scrapy.Field()
    source_country = scrapy.Field()
    site = scrapy.Field()
    context_identifier = scrapy.Field()
    record_create_by = scrapy.Field()
    execution_id = scrapy.Field()
    feed_code = scrapy.Field()

    pass
