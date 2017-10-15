from scrapy.mail import MailSender
from .helpers import config_section


def send_mail(body):
    '''Sends email
          :param body: The body of mail.
          :type string:
    '''
    # convert to str to escape issue in twisted
    server = str(config_section("mailer")['smtp_host'])
    mail_from = str(config_section("mailer")['mail_from'])
    user = str(config_section("mailer")['smtp_user'])
    password = str(config_section("mailer")['smtp_pass'])
    port = str(config_section("mailer")['smtp_port'])
    mailer = MailSender(server, mail_from, user, password, int(port), False,
                        False)
    recipient = str(config_section("mailer")['mail_to'])
    try:
        resp = mailer.send(to=recipient,
                    subject='Prodirect trainers', body=body, mimetype='text/html')
        return resp
    except:
        print(resp)