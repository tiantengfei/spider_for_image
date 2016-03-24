import scrapy
import time

from spider_for_image.items import SpiderForImageItem


class ImageSpider(scrapy.Spider):
    name = 'image_spider'

    def __init__(self, category=None, *args, **kwargs):
        print("category:" + category)
        self.start_urls = ['http://www.made-in-china.com/multi-search/%s/F1/1.html' % category]
        super(ImageSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        print('the length is {}'.format(len(response.xpath("//a[@class='img-thumb-inner']/img"))))
        for image_url in response.xpath("//a[@class='img-thumb-inner']/img"):
            image_item = SpiderForImageItem()
            # print(" my print is  {}:".format(image_url.xpath("@cz-id-300").extract()))
            ##   print("error: {}".format(image_url))
            # time.sleep(2)

            image_item['image_urls'] = image_url.xpath("@cz-id-300").extract()

            yield image_item

            next_pages = response.xpath('//a[@class="next"]/@href')

            for next_page in next_pages:
                print {"next page ..........."}
                url = response.urljoin(next_page.extract())
                yield scrapy.Request(url, self.parse)
