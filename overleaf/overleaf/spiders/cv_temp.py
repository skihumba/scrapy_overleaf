import scrapy


class CvTempSpider(scrapy.Spider):
    name = 'cv_temp'
    
    start_urls = ['https://www.overleaf.com/latex/templates/tagged/cv']

    def parse(self, response):
        for element in response.xpath('.//div[@class="gallery-thumbnail"]'):
            yield{
               'cv_url' : response.urljoin(element.xpath('.//a/@href').get()), 
               'cv_image_url' : element.xpath('.//img[@class="thumbnail"]/@src').get()
            }

        next_page_url = response.xpath('//a[@aria-label="Go to next page"]/@href').get()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))