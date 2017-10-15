from ..helpers import config_section
from .PageSpider import PageSpider

SIZE = config_section("trainers_spider")['size']
CURRENCY = config_section("trainers_spider")['currency']


class TrainersSpider(PageSpider):
    name = 'trainers'
    start_urls = \
        [PageSpider.home_url + '/lists/trainers.aspx?listName=trainers&cur=' +
         CURRENCY + '&pp=96&o=lth&s=' + SIZE]
