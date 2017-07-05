import scrapy
from jinja2 import Template
import configparser

class TrainersSpider(scrapy.Spider):
    name = 'trainers'
    home_url = 'http://www.prodirectselect.com'
    start_urls = \
        [home_url + '/lists/trainers.aspx?listName=trainers&cur=EUR&pp=96&o=lth&s=7,8']

    def config_section(self, section):
        config = configparser.ConfigParser()
        config.read("ProdirectScraper/configuration.ini")
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
                if dict1[option] == -1:
                    print "skip: %s" % option
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    def send_mail(self, body):
        from scrapy.mail import MailSender
        # convert to str to escape issue in twisted
        server = str(self.config_section("mailer")['smtp_host'])
        mail_from = str(self.config_section("mailer")['mail_from'])
        user = str(self.config_section("mailer")['smtp_user'])
        password = str(self.config_section("mailer")['smtp_pass'])
        port = str(self.config_section("mailer")['smtp_port'])
        mailer = MailSender(server, mail_from, user, password, int(port), False, False)
        mailer.send(to='zoran.pandovski@gmail.com', subject='Some subject',
                    body=body, mimetype='text/html')

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
        self.send_mail(table.encode('utf-8'))

