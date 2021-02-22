# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MarcaItem(scrapy.Item):

    marca = scrapy.Field()
    modelo = scrapy.Field()

    pass

class ModeloItem(scrapy.Item):

    anyo = scrapy.Field()
    nombre = scrapy.Field()

    pass

class SelectsItem(scrapy.Item):

    marca = scrapy.Field()
    pass

class ModelosItem(scrapy.Item):

    modelo = scrapy.Field()
    pass

