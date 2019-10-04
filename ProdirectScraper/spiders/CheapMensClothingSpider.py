from ..helpers import Configuration
from .PageSpider import PageSpider


class CheapMensClothingSpider(PageSpider):
    '''
      Spider that gets clothes for men's from http://www.prodirectselect.com/
       '''
    name = 'mensclothing'
    config = Configuration('mensclothing_spider')
    start_urls = \
        [PageSpider.home_url +
         'lists/cheap-mens-clothing.aspx?cur=' + config.currency +
         '&pp=' + config.pp + '&o=lth&s=' + config.size]

