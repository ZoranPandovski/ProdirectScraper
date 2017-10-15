from ..helpers import config_section
from .PageScraper import PageSpider

SIZE = config_section("trainers_spider")['size']
CURRENCY = config_section("trainers_spider")['currency']


class TrainersSpider(PageSpider):
    name = 'trainers'
    home_url = 'http://www.prodirectselect.com'
    start_urls = \
        [home_url + '/lists/trainers.aspx?listName=trainers&cur=' +
         CURRENCY + '&pp=96&o=lth&s=' + SIZE]
