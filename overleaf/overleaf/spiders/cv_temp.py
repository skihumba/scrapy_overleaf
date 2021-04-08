import scrapy


class CvTempSpider(scrapy.Spider):
    name = 'cv_temp'
    
    start_urls = ['https://www.overleaf.com/latex/templates/tagged/cv']

    def parse(self, response):
        pass
