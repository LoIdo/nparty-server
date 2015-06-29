import zope.interface


class IUser(zope.interface.Interface):
    """
    interface of user
    """

    id = zope.interface.Attribute('user id')
    ''' id of user '''

    name = zope.interface.Attribute('user name')
    ''' name of user '''

    mobile = zope.interface.Attribute('user mobile number')
    ''' mobile phone number of user '''

    address = zope.interface.Attribute('user address')
    ''' address of user '''


class ICenter(zope.interface.Interface):
    """
    interface of user center
    """

    def add_user(**kwargs):
        """
        add user by user information
        """

    def del_user(user_id):
        """
        remove user by user id
        """

    def get_user(user_id):
        """
        get user by user id
        """

    def find_users(**kwargs):
        """
        find users by user information
        """


class ICenterFactory(zope.interface.Interface):
    """
    interface of center factory
    """

    def __init__(bundle_factory):
        """
        :param bundle_factory:
        :return:
        """

    def __call__(bundle):
        """
        :param bundle:
        :return:
        """