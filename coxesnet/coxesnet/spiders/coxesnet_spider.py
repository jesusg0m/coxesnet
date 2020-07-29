import scrapy
from ..items import coxesnetItem

class WaluitSpiderSpider(scrapy.Spider):
    name = 'coxesnet'
    start_urls = ['https://www.coches.net/segunda-mano/']

    def parse(self, response):
        items = coxesnetItem()

        modelo = response.css('.mt-CardAd-titleHiglight::text').extract()
        precio = response.css('.mt-AdPrice-amount:nth-child(1) strong::text').extract()
        kms = response.css('.mt-CardAd-attribute:nth-child(4)::text').extract()
        anyo = response.css('.mt-CardAd-attribute:nth-child(3)::text').extract()


        items['modelo'] = modelo
        items['precio'] = precio
        items['kms'] = kms
        items['anyo'] = anyo

        yield items
