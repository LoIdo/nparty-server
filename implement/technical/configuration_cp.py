import ConfigParser

import zope.interface

import interface.technical.storage


class Storage(object):
    """
    class implements config interface
    """
    zope.interface.implements(interface.technical.storage.IStorage)
    
    def __init__(self):
        """ init all variables """
        self.config = ConfigParser.ConfigParser()
        self.config.read("nparty.conf")

    def setValue(self, key, value):
        keys = key.split(';', 1)
        if len(keys) > 1:
            self.config.set(keys[0], keys[1], value)
        else:
            self.config.set("server", keys[0], value)

    def getValue(self, key):
        keys = key.split(';', 1)
        if len(keys) > 1:
            self.config.get(keys[0], keys[1])
        else:
            self.config.get("server", keys[0])

    def updateValues(self):
        """ reload file """
        self.config.read("nparty.conf")
