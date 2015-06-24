import ConfigParser

import zope.interface.declarations

import interface.technical.config


@zope.interface.declarations.implementer(interface.technical.config.IConfig)
@zope.interface.declarations.provider(interface.technical.config.IConfigFactory)
class _Config(object):
    """
    class implements config interface
    """
    
    def __init__(self, filename, config):
        """ init all variables """
        self.filename = filename
        self.config = config

    def set_value(self, key, value):
        self.config.set('server', key, value)

    def get_value(self, key):
        return self.config.get('server', key)

    def update_values(self):
        """ reload file """
        self.config.read(self.filename)


class Factory(object):
    """
    factory of config interface
    """

    def __init__(self, bundle_factory):
        self.config = ConfigParser.ConfigParser()
        self.config.read(bundle_factory.other.conf_file)

    def __call__(self, bundle):
        """ create object provide interface """
        return _Config(bundle.other.conf_file, self.config)
