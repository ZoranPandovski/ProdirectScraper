from scrapy.mail import MailSender
from . import helpers


def send_mail(body):
    '''Sends email
          :param body: The body of mail.
          :type string:
    '''
    # convert to str to escape issue in twisted
    server = helpers.config_section("mailer")['smtp_host']
    mail_from = helpers.config_section("mailer")['mail_from']
    user = helpers.config_section("mailer")['smtp_user']
    password = helpers.config_section("mailer")['smtp_pass']
    port = helpers.config_section("mailer")['smtp_port']
    mailer = MailSender(server, mail_from, user, password, int(port), False,
                        False)
    recipient = helpers.config_section("mailer")['mail_to']
    try:
        resp = mailer.send(to=recipient,
                    subject='Prodirect trainers', body=body, mimetype='text/html')
        return resp
    except Exception as e:
        print(e.message)
