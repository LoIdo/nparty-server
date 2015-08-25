import base64
import uuid

import zope.interface
import zope.component

import interface.technical.token
import interface.technical.cache


class Center(object):
    """
    implement of token center
    """
    zope.interface.implements(interface.technical.token.IToken)

    def __init__(self):
        self.cache = zope.component.getUtility(
            interface.technical.cache.ICache)

    def addToken(self, value, timeout):
        list_token = self.cache.getKeys('token:*:%s' % value)
        if list_token:
            if len(list_token) > 1:
                return False  # incorrect token count
            self.cache.rmvKey(list_token[0])
        token = base64.urlsafe_b64encode(uuid.uuid4()).rstrip('=\n')
        token = "token:%s:%s" % (token, value)
        self.cache.setValue(token, "", timeout)
        return True

    def rmvToken(self, token_id):
        list_token = self.cache.getKeys('token:%s:*' % token_id)
        if list_token:  # remove all keys that match the token
            for key in list_token:
                self.cache.rmvKey(key)

    def rmvTokenMatch(self, token_id, value):
        list_token = self.cache.getKeys('token:%s:%s' % (token_id, value))
        if list_token:  # remove all keys that match the token
            for key in list_token:
                self.cache.rmvKey(key)

    def chkToken(self, token_id):
        list_token = self.cache.getKeys('token:%s:*' % token_id)
        if list_token and len(list_token) == 1:
            return list_token[0].split(':', 3)[2]