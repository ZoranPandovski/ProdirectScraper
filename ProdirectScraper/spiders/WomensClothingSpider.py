from ..helpers import Configuration
from .PageSpider import PageSpider


class WomensClothingSpider(PageSpider):
    '''
       Spider that gets clothes for women's from http://www.prodirectselect.com
    '''
    name = 'womensclothing'
    config = Configuration('womensclothing_spider')
    start_urls = \
        [PageSpider.home_url +
         'lists/womens-clothing.aspx?listname=mens-clothing&cur=' +
         config.currency + '&pp=32&pp=' + config.pp + '&o=lth&s='+ config.size]

