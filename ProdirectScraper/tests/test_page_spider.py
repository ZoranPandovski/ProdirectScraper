import unittest
import re
from scrapy.http import HtmlResponse, Response, Request
import spiders.PageSpider as PageSpider


def clean_html(html):
    '''
    remove whitespace between html tag
    '''
    return re.sub(r'>\s+<', '><', html).strip()


class TestPageSpider(unittest.TestCase):
    def setUp(self):
        self.page_spider = PageSpider.PageSpider('TestPageSpider')

    def test_parse(self):
        body = '''
            <div class="list"><div class="item">
            <p class="price">hello</p>
            <a href="foobar">hi</a>
            </div>
            </div>
            '''
        url='http://example.com'
        request = Request(url=url)
        response = HtmlResponse(url=url, request=request, body=unicode(body, 'utf-8'), encoding='utf-8')
        actual = self.page_spider.parse_helper(response)
        self.assertEqual(actual, [{'Price ': u'hello', 'More info ': u'http://www.prodirectselect.com/foobar', 'Description ': u'hi'}])


    def test_format_items(self):
        parsed_items = [
            {'Price': 1, 'Description': 'Item 1', 'More info': 'http://moreinfo-1'},
            {'Price': 2, 'Description': 'Item 2', 'More info': 'http://moreinfo-2'},
        ]
        expected_format = '''
        <table>
            <ul>
                <li>1</li>
                <li>http://moreinfo-1</li>
                <li>Item 1</li>
            </ul>
            <ul>
                <li>2</li>
                <li>http://moreinfo-2</li>
                <li>Item 2</li>
            </ul>
        </table>'''
        self.assertEqual(clean_html(self.page_spider.format_items(parsed_items)),
                         clean_html(expected_format))


