import zope.interface
import zope.component

import interface.account


class Account(object):

    zope.interface.implements(interface.account.IAccount)

