import unittest
from mock import mock

import scrapy
from scrapy.mail import MailSender


import emailer


class ServiceException(Exception):

    def __str__(self):
        return '{}: {}'.format(self.message, self.data if self.data else '')

    def __init__(self, message, data=None):
        self.message = message
        self.data = data
        super(ServiceException, self).__init__()


class TestEmailer(unittest.TestCase):

    def test_send_mail_success(self):
        # arrange
        # mail_sender.return_value = mail_sender_send
        body = '''
                <div class="list"><div class="item">
                <p class="price">hello</p>
                <a href="foobar">hi</a>
                </div>
                </div>
                '''

        # act
        with mock.patch.object(scrapy.mail.MailSender, 'send', return_value='Success'):
            response = emailer.send_mail(body)

        # assert
            self.assertEqual(response, 'Success')
