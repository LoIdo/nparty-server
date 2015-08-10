import redis
import zope.interface
import zope.component

import interface.technical.cache
import interface.technical.configuration


class Cache(object):
    """
    implements of cache center
    """
    zope.interface.implements(interface.technical.cache.ICache)

    def __init__(self):
        config = zope.component.getUtility(
            interface.technical.configuration)
        self.redis = redis.Redis(
            host=config.getValue('redis;host') or '127.0.0.1',
            port=config.getValue('redis;port') or '6379',
            password=config.getValue('redis;pwd') or '2v0eps4o')

    def getKeys(self, pattern):
        self.redis.keys(pattern=pattern)

    def setValue(self, key, value, expire):
        self.redis.setex(key, value, expire)

    def getValue(self, key):
        return self.redis.get(key)

    def swpValue(self, key, value, expire):
        val = self.redis.getset(key, value)
        if expire:  # set expire if there is any
            self.redis.expire(key, expire)
        return val

    def rmvKey(self, key):
        self.redis.delete(key)

    def rmvKeyMatch(self, key, value):
        with self.redis.pipeline() as p:
            while True:
                try:
                    p.watch(key)
                    if p.get(key) != value:
                        return False
                    p.multi()
                    p.delete(key)
                    p.execute()
                    return True
                except redis.WatchError:
                    continue