from scrapy.mail import MailSender
import helpers


def send_mail(body):
    '''Sends email
          :param body: The body of mail.
          :type string:
    '''
    # convert to str to escape issue in twisted
    server = str(helpers.config_section("mailer")['smtp_host'])
    mail_from = str(helpers.config_section("mailer")['mail_from'])
    user = str(helpers.config_section("mailer")['smtp_user'])
    password = str(helpers.config_section("mailer")['smtp_pass'])
    port = str(helpers.config_section("mailer")['smtp_port'])
    mailer = MailSender(server, mail_from, user, password, int(port), False,
                        False)
    recipient = str(helpers.config_section("mailer")['mail_to'])
    try:
        resp = mailer.send(to=recipient,
                    subject='Prodirect trainers', body=body, mimetype='text/html')
        return resp
    except Exception:
        print(resp)