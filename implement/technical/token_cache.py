import base64
import uuid

import zope.interface.declarations

import interface.technical.token


@zope.interface.declarations.implementer(interface.technical.token.ICenter)
@zope.interface.declarations.provider(interface.technical.token.ICenterFactory)
class _Center(object):
    """
    implement of token center
    """

    def __init__(self, cache):
        self.cache = cache

    def add_token(self, value, timeout):
        list_token = self.cache.get_keys('token:*:%s' % value)
        if list_token:
            if len(list_token) > 1:
                return False  # incorrect token count
            self.cache.rmv_key(list_token[0])
        token = base64.urlsafe_b64encode(uuid.uuid4()).rstrip('=\n')
        token = "token:%s:%s" % (token, value)
        self.cache.set_value(token, "", timeout)
        return True

    def rmv_token(self, token_id):
        list_token = self.cache.get_keys('token:%s:*' % token_id)
        if list_token:  # remove all keys that match the token
            for key in list_token:
                self.cache.rmv_key(key)

    def rmv_token_match(self, token_id, value):
        list_token = self.cache.get_keys('token:%s:%s' % (token_id, value))
        if list_token:  # remove all keys that match the token
            for key in list_token:
                self.cache.rmv_key(key)

    def chk_token(self, token_id):
        list_token = self.cache.get_keys('token:%s:*' % token_id)
        if list_token and len(list_token) == 1:
            return list_token[0].split(':', maxsplit=3)[2]


@zope.interface.declarations.implementer(interface.technical.token.ICenterFactory)
class Factory(object):
    """
    implement of factories
    """

    def __init__(self, bundle_factory):
        pass

    def __call__(self, bundle):
        """  create and return token center """
        return _Center(bundle.component.technical.cache)
