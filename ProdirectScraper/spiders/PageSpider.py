import scrapy
from jinja2 import Template
from ..emailer import send_mail


class PageSpider(scrapy.Spider):
    home_url = 'http://www.prodirectselect.com/'

    def parse(self, response):
        '''
        Parse the response downloaded for each of the
        requests made.
        :param response:  holds the page content
        :return:
        '''
        formatted_items = self.format_items(self.parse_helper(response))
        send_mail(formatted_items.encode('utf-8'))

    def parse_helper(self, response):
        '''
        Parse the html returned from spider
        :param response:
        :return: items list
        '''
        collection = []
        for item in response.css('div.list div.item'):
            trainers = {
                'Price ': item.css('p.price::text').extract_first(),
                'Description ': item.css('a::text').extract_first(),
                'More info ': self.home_url +
                item.css('a::attr(href)').extract_first()
            }
            collection.append(trainers)

        return collection

    def format_items(self, items):
        '''
        Create html table to display the items
        :param items:
        :return: Html table
        '''
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
        formatted_items = template.render(items=items)
        return formatted_items
