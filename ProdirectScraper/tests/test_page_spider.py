import unittest
import re

import spiders.PageSpider as PageSpider


class TestPageSpider(unittest.TestCase):
    def setUp(self):
        self.page_spider = PageSpider.PageSpider('TestPageSpider')

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
        self.assertEqual(self.clean_html(self.page_spider.format_items(parsed_items)),
                         self.clean_html(expected_format))

    def clean_html(self, html):
        '''
        remove whitespace between html tag
        '''
        return re.sub(r'>\s+<', '><', html).strip()
