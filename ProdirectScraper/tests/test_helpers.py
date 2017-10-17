import unittest
from ..helpers import config_section


class TestConfigOptions(unittest.TestCase):

    def test_config_section_size_value(self):
        #arrange

        #act
        config_size = config_section("trainers_spider")['size']
        sizes = config_size.split(",")

        #assert
        for size in sizes:
            self.assertTrue(4 <= int(size) <= 14)

    def test_config_section_currency(self):
        #arrange
        currencies = ['EUR', 'USD', 'GBP']
        flag = False

        #act
        config_curr = config_section("general")['currency']
        if config_curr in currencies:
            flag = True

        #assert
        self.assertTrue(flag)

    def test_config_section_mailer(self):
        #arrange

        #act
        config_to = config_section("mailer")['mail_to']

        #assert
        self.assertIsNot(config_to, '')

if __name__ == '__main__':
    unittest.main()