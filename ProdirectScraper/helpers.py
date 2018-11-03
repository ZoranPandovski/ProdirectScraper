import configparser


class Configuration:

    def __init__(self, spider):
        self.size = config_section(spider)['size']
        self.currency =  config_section("general")['currency']
        self.pp = config_section("general")['pp']


def config_section(section):
    '''
    Read configuration properties
    :param section: configuration section
    :return:
    '''
    config = configparser.ConfigParser()
    config.read("configuration.ini")
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = str(config.get(section, option))
            if dict1[option] == -1:
                continue
        except Exception as e:
            print e.message
            dict1[option] = None
    return dict1
