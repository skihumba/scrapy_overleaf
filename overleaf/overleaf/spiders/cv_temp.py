import scrapy


class CvTempSpider(scrapy.Spider):
    name = 'cv_temp'
    
    start_urls = ['https://www.overleaf.com/latex/templates/tagged/cv']

    def parse(self, response):
        # links =  response.xpath('//div[@class="gallery-thumbnail"]/a/@href').extract()
        # for link in links:
        #     self.log(response.urljoin(link))
        # images = response.xpath('//img[@class="thumbnail"]/@src').extract()
        # for img in images:
        #     self.log(img)
        for element in response.xpath('.//div[@class="gallery-thumbnail"]'):
            # yield{
            # #    'cv_url' : response.urljoin(i for i in response.xpath('//div[@class="gallery-thumbnail"]/a/@href').extract()), 
            # #    'cv_url' : response.urljoin(element.xpath('.//div[@class="gallery-thumbnail"]/a/@href').extract()),
            # #    'cv_url' : element.xpath('.//div[@class="gallery-thumbnail"]/a/@href').extract(),
            #    'cv_image_url' : element.xpath('.//img[@class="thumbnail"]/@src').extract()
            # }

            # cv_url = response.urljoin(response.xpath('//div[@class="gallery-thumbnail"]/a/@href').extract())
            # self.log(cv_url)

            # cv_url = response.urljoin(str(element.xpath('.//a/@href').extract())) <--PROMISING!!
            tmp_cv_url = element.xpath('.//a/@href').extract()
            cv_url = response.urljoin(tmp_cv_url)
            # cv_url = response.urljoin(temp_cv_url)

            cv_image_url = element.xpath('.//img[@class="thumbnail"]/@src').extract()

            yield {
                'cv_url' : cv_url,
                'cv_image_url' : cv_image_url
            }
