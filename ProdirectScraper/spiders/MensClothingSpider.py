from ..helpers import config_section
from .PageScraper import PageSpider

SIZE = config_section("mensclothing_spider")['size']
CURRENCY = config_section("mensclothing_spider")['currency']


class MensClothingSpider(PageSpider):
    name = 'mensclothing'
    home_url = 'http://www.prodirectselect.com/'
    start_urls = \
        [home_url + 'lists/mens-clothing.aspx?listName=mens-clothing&cur=' +
         CURRENCY + '&pp=32&pp=96&o=lth&s=' + SIZE]
