from ..helpers import config_section
from .PageSpider import PageSpider

SIZE = config_section("mensclothing_spider")['size']
CURRENCY = config_section("general")['currency']
PP = config_section("general")['pp']


class MensClothingSpider(PageSpider):
    name = 'womensclothing'
    start_urls = \
        [PageSpider.home_url + 'lists/womens-clothing.aspx?listName=mens-clothing&cur=' +
         CURRENCY + '&pp=32&pp=' + PP + '&o=lth&s=' + SIZE]

