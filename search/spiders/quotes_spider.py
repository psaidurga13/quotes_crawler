

import scrapy

class QuotesSpider(scrapy.Spider):

    name = "quotes"
    next_url = ''

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/'
                    ]

        for url in urls:
            yield scrapy.Request(url = url , callback = self.parse)

    def parse(self,response):
        src = response.xpath('//div[@class="row"]/div[@class = "col-md-8"]')

        a = src.xpath('./div[@class = "quote"]')

        for i in a:
            yield{
                'author':i.xpath('./span/small[@class = "author"]/text()').extract()[0].encode('utf-8'),
                'quote':i.xpath('./span[@class = "text"]/text()').extract()[0].encode('utf-8')
                }

        next_url = response.xpath('//nav/ul[@class = "pager"]/li[@class="next"]/a/@href').extract()[0].encode('utf-8')
        if next_url is not None:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url = next_url,callback = self.parse)


