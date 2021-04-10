import scrapy


class CvTempSpider(scrapy.Spider):
    name = 'cv_temp'
    
    start_urls = ['https://www.overleaf.com/latex/templates/tagged/cv']

    def parse(self, response):
        for element in response.xpath('.//div[@class="gallery-thumbnail"]'):
            cv_url = response.urljoin(element.xpath('.//a/@href').get())
            cv_image_url = element.xpath('.//img[@class="thumbnail"]/@src').get()

            yield{
               'cv_url' : cv_url, 
               'cv_image_url' : cv_image_url
            }

            # next page(s)
            next_page_url = response.xpath('//a[@aria-label="Go to next page"]/@href').get()
            if next_page_url is not None:
                yield response.follow(response.urljoin(next_page_url), callback=self.parse)

            # create web page with cv images as hyperlinks to the cv url
            html = ""
            html += """<a href="{cv_url}"
            target="_blank">
            <img src="{cv_image_url}" height="50%" width="30%"/>
            <a/>.
            """.format(cv_url=cv_url, cv_image_url=cv_image_url)

            with open("./data/cv_templates.html", mode="a") as web_page:
                web_page.write(html)
                web_page.close()