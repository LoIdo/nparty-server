import zope.interface


class IUser(zope.interface.Interface):
    """
    interface of user authentication
    """
    account = zope.interface.Attribute('account to login')

    password = zope.interface.Attribute('password to login')

    mobile = zope.interface.Attribute('binding mobile number')

    email = zope.interface.Attribute('binding primary email')

    email_backup = zope.interface.Attribute('binding backup email')

    name = zope.interface.Attribute('user name')
    ''' name of user '''

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