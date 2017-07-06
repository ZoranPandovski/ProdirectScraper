import scrapy
from jinja2 import Template
from ..emailer import send_mail

class TrainersSpider(scrapy.Spider):
    name = 'trainers'
    home_url = 'http://www.prodirectselect.com'
    start_urls = \
        [home_url + '/lists/trainers.aspx?listName=trainers&cur=EUR&pp=96&o=lth&s=7,8']

    def parse(self, response):
        collection = []
        for item in response.css('div.list div.item'):
            trainers = {
                'Price ': item.css('p.price::text').extract_first(),
                'Description ': item.css('a::text').extract_first(),
                'More info ': self.home_url +
                              item.css('a::attr(href)').extract_first()
            }
            collection.append(trainers)

        template = Template("""
        <table>
            {% for item in items %}
                 <ul>
                 {% for key, value in item.items() %}
                    {% if value %}
                       <li>{{value}}</li>
                    {% endif %}
                {% endfor %}
                </ul>
            {% endfor %}
        </table>
        """)
        table = template.render(items=collection)
        send_mail(table.encode('utf-8'))

