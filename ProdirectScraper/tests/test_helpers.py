import unittest
import helpers


class TestConfigOptions(unittest.TestCase):

    def test_config_section_size_value(self):
        #arrange

        #act
        config_size = helpers.config_section("trainers_spider")['size']
        sizes = config_size.split(",")

        #assert
        for size in sizes:
            self.assertTrue(4 <= int(size) <= 14)

    def test_config_section_currency(self):
        #arrange
        currencies = ['EUR', 'USD', 'GBP']
        flag = False

        #act
        config_curr = helpers.config_section("general")['currency']
        if config_curr in currencies:
            flag = True

        #assert
        self.assertTrue(flag)

    def test_config_section_mailer(self):
        #arrange

        #act
        config_to = helpers.config_section("mailer")['mail_to']

        #assert
        self.assertIsNot(config_to, '')

    def test_configuration(self):
        #arrange

        #act
        config = helpers.Configuration('mensclothing_spider')

        #assert
        self.assertIsNot(config.size, '')

if __name__ == '__main__':
    unittest.main()
