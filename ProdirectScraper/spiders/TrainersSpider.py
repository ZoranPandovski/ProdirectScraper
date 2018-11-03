from ..helpers import Configuration
from .PageSpider import PageSpider


class TrainersSpider(PageSpider):
    name = 'trainers'
    config = Configuration('trainers_spider')
    start_urls = \
        [PageSpider.home_url + '/lists/trainers.aspx?listName=trainers&cur=' +
         config.currency + '&pp=' + config.pp + '&o=lth&s=' + config.size]
