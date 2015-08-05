import zope.interface


class ICache(zope.interface.Interface):
    """
    interface of cache center
    wrapper of sth. like memcache and redis
    """

    def getKeys(pattern):
        """
        get keys by pattern
        """

    def setValue(key, value, expire):
        """
        set key value pair to cache
        """

    def getValue(key):
        """
        get value by key in cache
        """

    def swpValue(key, value, expire):
        """
        swap value, if there is already key value pair in cache
        """

    def rmvKey(key):
        """
        remove key value pair in cache
        """

    def rmvKeyMatch(key, value):
        """
        remove key value pair in cache if the input is matched
        """