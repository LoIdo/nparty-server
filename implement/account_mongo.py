import zope.interface
import zope.component

import interface.account
import interface.technical.storage
import interface.technical.database


class Account(object):

    zope.interface.implements(interface.account.IAccount)

    def get_id(self):
        return self._cache.get('_id')

    def get_name(self):
        return self._cache.get('name')

    def get_password(self):
        return self._cache.get('password')

    def set_password(self, pswd):
        self._cache['password'] = pswd

    id = property(fget=get_id, doc='id of account')
    name = property(fget=get_name, doc='name of account')
    password = property(fget=get_password, fset=set_password, doc='password of account')

    def __init__(self, collection, cache=None):
        self._cache = cache or {}
        self._collection = collection

    def remove(self):
        self._collection.remove(
            {'_id': self.get_id()})

    def setValue(self, key, value):
        profile = self._cache.get('profile')
        if not isinstance(profile, dict):
            profile = dict()
            self._cache['profile'] = profile
        self._collection.update(
            {'_id': self.get_id()},
            {'$set': {'profile.%s' % key: value}})

    def getValue(self, key):
        profile = self._cache.get('profile')
        return profile.get(key)\
            if isinstance(profile, dict) else None

    def updateValues(self):
        self._cache = self._collection.find_one(
            {'_id': self.get_id()})


class Center(object):

    zope.interface.implements(interface.account.ICenter)
    zope.component.adapts(interface.technical.database.IOperator)

    def __init__(self, operator):
        self.collection = operator.accounts
        self.collection.ensure_index('name')
        ''' treat operator as pymongo Database'''

    def addAccount(self, name, password, **kwargs):
        if not password:
            ''' check account name only '''
            return bool(self.collection.find_one({"name": name}))
        else:
            cache = {'name': name, 'password': password, 'profile': kwargs}
            object_id = self.collection.insert_one(cache).inserted_id
            cache['_id'] = object_id
            return Account(self.collection, cache)

    def getAccount(self, name):
        cache = self.collection.find_one({'name': name})
        return cache and Account(self.collection, cache)

