import zope.interface


class IAccount(zope.interface.Interface):
    """
    interface for account
    """

    id = zope.interface.Attribute('id of account')
    ''' id of account '''

    def getProfile(key):
        """
        get profile of account
        """

    def setProfile(key, value):
        """
        get profile of account
        """


class ICenter(zope.interface.Interface):
    """
    center of account
    """

    def addAccount(account, password, **kwargs):
        """
        :param account:
        :param password:
        :return:
        """

    def rmvAccount(account_id):
        """
        :param account:
        :return:
        """

    def authAccount(account, password):
        """
        authenticate for account
        :param account:
        :param password:
        :return:
        """