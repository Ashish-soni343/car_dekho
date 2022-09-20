import scrapy
import datetime
from ..items import CardekhoScrapingItem

class CarDekhoSpider(scrapy.Spider):

    name = 'car_dekho'
    allowed_domains = ['www.cardekho.com']
    start_url = 'https://www.cardekho.com/new-cars+20-lakh-35-lakh'

    # Mandatory data
    #AEID_project_id = ''
    site = 'www.cardekho.com'
    source_country = 'IN'
    context_identifier = 'cars available in range of price 20 to 35 lakhs INR in India'
    file_create_dt = datetime.datetime.utcnow().strftime('%Y-%m-%d %T')[0:10]
    file_name = name + "_" + file_create_dt
    record_created_by = "12345_car_dekho_price_range"
    execution_id = "620224"                # This will be taken automatically from zyte, for now this is hardcoded
    feed_code = "12345"


    # settings for Crawling
    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'CONCURRENT_REQUESTS': 4,
        "DOWNLOADER_MIDDLEWARES":{
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
            },                                                # used for IP rotation
        "AUTOTHROTTLE_ENABLED": True,
        "DOWNLOAD_TIMEOUT": 600
        }

    def start_requests(self):                 # function to crawl the given website

        yield scrapy.Request(
            url=self.start_url,
            callback=self.parse_cars
            )

    def parse_cars(self, response):           # funtion to fetch url for each car


        cars = response.css('h3 a::attr(href)').extract()

        for car in cars:
            yield scrapy.Request(
                url=f"https://www.cardekho.com{car}",
                callback=self.parse_cars_detail
                )


    def parse_cars_detail(self, response):          # Function to extract data from fetched urls

        item = CardekhoScrapingItem()               # object to store data in "items.py"

        car = (response.css(".tooltip::text").get())
        specification_i = response.css('#specification span , #specification td::text').getall()
        specification_u = [s.replace("<span>", "").replace("</span>", "") for s in specification_i]
        specification = {specification_u[s-1] : specification_u[s] for s in range(1,len(specification_u),2)}

        # Data scraped
        item["record_create_dt"] = datetime.datetime.utcnow().strftime('%Y-%m-%d %T')
        item["car"] = car
        item["feed_code"] = self.feed_code
        item["site"] = self.site
        item["source_country"] = self.source_country
        item["context_identifier"] = self.context_identifier
        item["record_create_by"] = self.record_created_by
        item["execution_id"] = self.execution_id
        item["specification"] = specification
        item["src"] = response.url

        yield item