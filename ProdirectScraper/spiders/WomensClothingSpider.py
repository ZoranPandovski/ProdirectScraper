from ..helpers import config_section
from .PageSpider import PageSpider

SIZE = config_section("mensclothing_spider")['size']
CURRENCY = config_section("mensclothing_spider")['currency']


class MensClothingSpider(PageSpider):
    name = 'womensclothing'
    start_urls = \
        [PageSpider.home_url + 'lists/womens-clothing.aspx?listName=mens-clothing&cur=' +
         CURRENCY + '&pp=32&pp=96&o=lth&s=' + SIZE]

