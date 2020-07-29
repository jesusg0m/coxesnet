# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class coxesnetItem(scrapy.Item):
    # define the fields for your item here like:
    modelo = scrapy.Field()
    precio = scrapy.Field()
    kms = scrapy.Field()
    anyo = scrapy.Field()
    pass
