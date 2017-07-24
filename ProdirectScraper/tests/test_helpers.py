import unittest
import helpers as h

class TestConfigOptions(unittest.TestCase):

    def test_config_section_size_value(self):
        #arrange

        #act
        config_size = h.config_section("trainers_spider")['size']
        sizes = config_size.split(",")

        #assert
        for size in sizes:
            self.assertTrue(4 <= int(size) <= 14)

    def test_config_section_mailer(self):
        #arrange
        to = 'zoran.pandovski@gmail.com'

        #act
        config_to = h.config_section("mailer")['mail_to']

        #assert
        self.assertEqual(to, config_to)

if __name__ == '__main__':
    unittest.main()
