import zope.interface


class IStorage(zope.interface.Interface):
    """
    center of storage
    """

    def addStorage(name, stream):
        """
        add storage
        return url
        """

    def delStorage(url):
        """
        delete storage
        """

    def findStorage(pattern):
        """
        find storage
        return list of url
        """