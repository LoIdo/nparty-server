import zope.interface

import interface.technical.storage


class IAccount(interface.technical.storage.IStorage):
    """
    interface for account, inherit IStorage interface
    """

    id = zope.interface.Attribute('id of account')
    ''' id of account '''

    name = zope.interface.Attribute('account name')
    ''' name of account '''

    password = zope.interface.Attribute('account password')
    ''' password of account '''

    def remove():
        """
        remove current account
        """


class ICenter(zope.interface.Interface):
    """
    center of account
    """

    def addAccount(name, password, **kwargs):
        """
        :param account:
        :param password:
        :return:
        """

    def getAccount(name):
        """
        authenticate for account
        :param account:
        :param password:
        :return:
        """