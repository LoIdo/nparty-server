import zope.interface


class ICenter(zope.interface.Interface):
    """
    configuration center interface
    """

    def set_value(key, value):
        """
        add key value pair to configuration
        """

    def get_value(key):
        """
        query value by key
        """

    def update_values():
        """
        update all values from configuration
        """


class ICenterFactory(zope.interface.Interface):
    """
    config center interface factory
    """

    def __init__(bundle_factory):
        """
        initialize center factory by bundle factory
        """

    def __call__(bundle):
        """
        create an object which provide config center interface
        """
