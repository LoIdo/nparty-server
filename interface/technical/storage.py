import zope.interface


class IStorage(zope.interface.Interface):
    """
    configuration center interface
    """

    def setValue(key, value):
        """
        add key value pair to configuration
        """

    def getValue(key):
        """
        query value by key
        """

    def updateValues():
        """
        update all values from configuration
        """