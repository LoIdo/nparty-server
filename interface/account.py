import zope.interface


class IAccount(zope.interface.Interface):
    """
    interface for account
    """

    id = zope.interface.Attribute('id of account')
    ''' id of account '''

    name = zope.interface.Attribute('account name')
    ''' name of account '''

    profile = zope.interface.Attribute('account profile')
    ''' profile of account, provide interface.technical.storage.IStorage '''


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

    def rmvAccount(account):
        """
        :param account:
        :return:
        """

    def authAccount(name, password):
        """
        authenticate for account
        :param account:
        :param password:
        :return:
        """