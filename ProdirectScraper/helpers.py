import configparser


def config_section(section):
    '''
    Read configuration properties
    :param section: configuration section
    :return:
    '''
    config = configparser.ConfigParser()
    config.read("ProdirectScraper/configuration.ini")
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                print "skip: %s" % option
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1