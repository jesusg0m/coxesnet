import scrapy
from ..items import SelectsItem, ModelosItem, MarcaItem, ModeloItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule




class MarcasSpider(scrapy.Spider):
    name = 'marcas'
    start_urls = ['https://www.back4app.com/database/back4app/car-make-model-dataset/all-cars-by-model-and-by-make-and-by-year']

    def parse(self, response):
        items = MarcaItem()

        #marca = response.xpath('//li[@class="react-autocomplete__list-item"]').extract()
        marca = response.css('.text-nowrap:nth-child(1) .text-truncate::text').extract()
        nombre = response.css('.text-nowrap:nth-child(2) .text-truncate::text').extract()
        anyo = response.css('.text-nowrap:nth-child(4) .text-truncate::text').extract()


        s1 = ModeloItem()
        s1['nombre'] = nombre
        s1['anyo'] = anyo

        items['marca'] = marca
        items['modelo'] = [dict(s1)]
        yield items









class ModelosSpider(scrapy.Spider):
    name = 'modelos'
    start_urls = ['https://www.eleconomista.es/ecomotor/coche/VOLVO']

    def parse(self, response):
        items = ModelosItem()

        #marca = response.xpath('//li[@class="react-autocomplete__list-item"]').extract()
        modelo = response.css('.t-coche li a::text').extract()

        items['modelo'] = modelo
        yield items