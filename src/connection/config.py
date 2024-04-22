from configparser import ConfigParser


def get_config_param(filename='../../database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        return dict((x, y) for x, y in parser.items(section))

    raise Exception('Section {0} not found in the {1} file'.format(section, filename))


if __name__ == '__main__':
    config = get_config_param()
    print(config)

