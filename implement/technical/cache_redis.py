import redis
import zope.interface.declarations

import interface.technical.cache
import interface.technical.config
import implement.technical


@zope.interface.declarations.implementer(interface.technical.cache.ICache)
@zope.interface.declarations.provider(interface.technical.cache.ICacheFactory)
class _Cache(object):
    """
    implements of cache center
    """

    def __init__(self, engine_redis):
        self.engine_redis = engine_redis

    def get_keys(self, pattern):
        self.engine_redis.keys(pattern=pattern)

    def set_value(self, key, value, expire):
        self.engine_redis.setex(key, value, expire)

    def get_value(self, key):
        return self.engine_redis.get(key)

    def swp_value(self, key, value, expire):
        val = self.engine_redis.getset(key, value)
        if expire:  # set expire if there is any
            self.engine_redis.expire(key, expire)
        return val

    def rmv_key(self, key):
        self.engine_redis.delete(key)

    def rmv_key_match(self, key, value):
        with self.engine_redis.pipeline() as p:
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


@zope.interface.declarations.implementer(interface.technical.cache.ICacheFactory)
class Factory(object):
    """
    implements of verify code center factory
    """
    def __init__(self, bundle_factory):
        """ initialize redis """
        config = bundle_factory.component.technical.config(bundle_factory())
        if not interface.technical.config.IConfig.providedBy(config):
            raise Exception('invalid configuration center')

        bundle_factory.dependent.redis = implement.technical.Dummy()
        bundle_factory.dependent.redis.engine = redis.Redis(
            host=config.get_value('redis_host') or '127.0.0.1',
            port=config.get_value('redis_port') or '6379',
            password=config.get_value('redis_pwd') or '2v0eps4o')

    def __call__(self, bundle):
        return _Cache(bundle.dependent.redis.engine)