import zope.interface


class ICenter(zope.interface.Interface):
    """
    interface of cache center
    wrapper of sth. like memcache and redis
    """

    def set_value(key, value, expire):
        """
        set key value pair to cache
        """

    def get_value(key):
        """
        get value by key in cache
        """

    def swp_value(key, value, expire):
        """
        swap value, if there is already key value pair in cache
        """

    def rmv_value(key):
        """
        remove key value pair in cache
        """

    def rmv_value_match(key, value):
        """
        remove key value pair in cache if the input is matched
        """


class ICenterFactory(zope.interface.Interface):
    """
    cache center interface factory
    """

    def __init__(bundle_factory):
        """
        initialize center factory by bundle factory
        """

    def __call__(bundle):
        """
        create an object which provide cache center interface
        """