import scrapy
from datetime import date
from ..items import CardekhoItem


class CarDekhoSpider(scrapy.Spider):
    name = 'car_dekho'
    project_id = 'carID123'

    # Settings for deployment in zyte:

    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'CONCURRENT_REQUESTS': 2,
        # using user-agents to rotate IPs:
        "DOWNLOADER_MIDDLEWARES": {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        },
        "AUTOTHROTTLE_ENABLED": True,
        "DOWNLOAD_TIMEOUT": 600
    }
    allowed_domains = ['www.cardekho.com']
    start_urls = ['https://www.cardekho.com/usedCars']

    def parse(self, response):
        items = CardekhoItem()  # Object to store data in items.py
        cars = response.css('.holder')  # Selecting product container
        for car in cars:
            selector = scrapy.Selector(text=car.get())
            car_title = selector.css('.title::text').get()
            price_blurb = selector.css('.price::text').extract().pop(1)
            fuel_type = selector.css('.dotlist span:nth-child(2)::text').get()
            gear_box = selector.css('span~ span+ span::text').get()
            variant = selector.css('div.variant::text').get()
            mileage = selector.css('.dotlist span:nth-child(1)::text').get()

            items['car_title'] = car_title
            items['price_blurb'] = price_blurb
            items['fuel_type'] = fuel_type
            items['gear_box'] = gear_box
            items['variant'] = variant
            items['mileage'] = mileage
            items['record_create_date'] = str(date.today())
            items['site'] = 'www.cardekho.com'
            items['source_country'] = 'IND'
            items['feed_code'] = 'carID123'
            items['context_identifier'] = 'Used car in india'
            items['record_create_by'] = 'carID123_cardekho_usedcar'
            items['execution_id'] = '620115'  # This will be taken automatically from zyte , as of now this is hardcoded

            yield items
