import zope.interface


class IStorage(zope.interface.Interface):
    """
    center of storage
    """

    def add_storage(name, stream):
        """
        add storage
        return url
        """

    def del_storage(url):
        """
        delete storage
        """

    def find_storage(pattern):
        """
        find storage
        return list of url
        """


class IStorageFactory(zope.interface.Interface):
    """
    storage center interface factory
    """
    def __init__(bundle_factory):
        """
        initialize factory
        """

    def __call__(bundle):
        """
        create an object which provide moments center interface
        """