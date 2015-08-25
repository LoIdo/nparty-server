import argparse

import zope.interface

import interface.technical.storage


class Storage(object):
    """
    argparse implements for storage interface
    """
    zope.interface.implements(interface.technical.storage.IStorage)

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--debug', nargs="?", default=argparse.SUPPRESS)
        parser.add_argument('--file', default="default.conf")
        self.arg = parser.parse_args()

    def setValue(self, key, value):
        """
        should not implement setValue
        """
        raise NotImplementedError

    def getValue(self, key):
        try:
            return getattr(self.arg, key)
        except AttributeError:
            return None

    def updateValues(self):
        """
        should not implement updateValues
        """
        raise NotImplementedError