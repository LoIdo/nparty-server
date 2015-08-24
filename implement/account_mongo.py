import zope.interface
import zope.component

import interface.account
import interface.technical.storage
import interface.technical.database


class Profile(object):

    zope.interface.implements(interface.technical.storage.IStorage)

    def __init__(self, collection, cache=None):
        self._collection = collection
        self._dict = cache or {}

    def setValue(self, key, value):
        self._dict[key] = value
        self._collection.update()

    def getValue(self, key):
        pass

    def updateValues(self):
        pass


class Account(object):

    zope.interface.implements(interface.account.IAccount)

    def __init__(self):
        self._id = None
        self._name = None
        self._pswd = None
        self._profile = None

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_profile(self):
        return self._profile

    id = property(fget=get_id(), doc='id of account')
    name = property(fget=get_name(), doc='name of account')
    profile = property(fget=get_profile(), doc='profile of account')


class Center(object):

    zope.interface.implements(interface.account.ICenter)
    zope.component.adapts(interface.technical.database.IOperator)

    def __init__(self, operator):
        self.collection = operator.accounts
        ''' treat operator as pymongo Database'''

    def addAccount(self, name, password, **kwargs):
        acc = Account(self.collection)
        acc.update(**{'account': name, 'password': password})
        acc.update(**kwargs)
        acc.update(_id=self.collection.insert_one(acc).inserted_id)
        return acc

    def rmvAccount(self, account):
        pass

    def authAccount(self, name, password):
        pass