import zope.interface


class IAuth(zope.interface.Interface):
    """
    interface of user authentication
    """

    password = zope.interface.Attribute('password to login')

    mobile = zope.interface.Attribute('binding mobile number')

    email = zope.interface.Attribute('binding primary email')

    email_backup = zope.interface.Attribute('binding backup email')


class IProfile(zope.interface.Interface):
    """
    interface of user profile
    """

    name = zope.interface.Attribute('user name')
    ''' name of user '''

    address = zope.interface.Attribute('user address')
    ''' address of user '''


class IUser(zope.interface.Interface):
    """
    interface of user
    """

    id = zope.interface.Attribute('user id')
    ''' id of user '''

    profile = zope.interface.Attribute('user profile')
    ''' user profile, should provide interface.user.IProfile '''

    authentication = zope.interface.Attribute('user authentication')
    ''' user authentication, should provide interface.user.IAuth '''

    schedule = zope.interface.Attribute('user schedule')
    ''' user schedule, should provide interface.schedule.ISchedule '''


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