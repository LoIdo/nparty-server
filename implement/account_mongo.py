import zope.interface
import zope.component

import interface.account
import interface.technical.database


class Account(dict):

    zope.interface.implements(interface.account.IAccount)

    def __init__(self, collection):
        super(Account, self).__init__()
        self.collection = collection

    def get_id(self):
        return self.get('_id')

    id = property(fget=get_id(), doc='id of account')

    def getProfile(self, key):
        """ get profile of account """
        return self.get(key)

    def setProfile(self, key, value):
        v = self.get(key)
        self[key] = value
        # self.collection.update()


class Center(object):

    zope.interface.implements(interface.account.ICenter)
    zope.component.adapts(interface.technical.database.IOperator)

    def __init__(self, operator):
        self.collection = operator.accounts
        ''' treat operator as pymongo Database'''

    def addAccount(self, account, password, **kwargs):
        acc = Account(self.collection)
        acc.update(**{'account': account, 'password': password})
        acc.update(**kwargs)
        acc.update(_id=self.collection.insert_one(acc).inserted_id)
        return acc

    def rmvAccount(self, account_id):
        pass

    def authAccount(self, account, password):
        pass