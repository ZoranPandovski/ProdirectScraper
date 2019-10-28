from ..helpers import Configuration
from .PageSpider import PageSpider


class MensClothingSpider(PageSpider):
    '''
      Spider that gets clothes for men's from http://www.prodirectselect.com/
       '''
    name = 'mensclothing'
    config = Configuration('mensclothing_spider')
    start_urls = \
        [PageSpider.home_url +
         'lists/mens-clothing.aspx?listname=mens-clothing&cur=' +
         config.currency + '&pp=' + config.pp + '&o=lth&s=' + (config.size).replace(',','&s=')]

