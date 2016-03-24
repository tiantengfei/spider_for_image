import scrapy

class ImageUrlSpider(scrapy.Spider):

    name = 'image_url_spider'
    start_urls = ['http://www.made-in-china.com/productdirectory.do?word=scooter&subaction=hunt&'
                  'style=b&mode=and&code=0&comProvince=nolimit&order=0&isOpenCorrection=1']

    def parse(self, response):

        print("eeeeee.....")
        for src in response.xpath("//a[@class='img-thumb-inner']/img"):

            print('start')
            print src.xpath("@src").extract(), src.xpath("@class").extract()
