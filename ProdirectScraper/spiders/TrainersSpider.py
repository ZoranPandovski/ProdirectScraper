from ..helpers import config_section
from .PageSpider import PageSpider

SIZE = config_section("trainers_spider")['size']
CURRENCY = config_section("general")['currency']
PP = config_section("general")['pp']


class TrainersSpider(PageSpider):
    name = 'trainers'
    start_urls = \
        [PageSpider.home_url + '/lists/trainers.aspx?listName=trainers&cur=' +
         CURRENCY + '&pp=' + PP + '&o=lth&s=' + SIZE]
