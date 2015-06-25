import zope.interface


class ICenter(zope.interface.Interface):
    """
    center of access token
    """

    def add_token(value, timeout):
        """
        generate access token by value
        same value mapping to only one token
        return token id
        """

    def rmv_token(token_id):
        """
        remove access token by id
        """

    def rmv_token_match(token_id, value):
        """
        remove access token by id
        and while value is match
        """

    def chk_token(token_id):
        """
        check value of token
        """


class ICenterFactory(zope.interface.Interface):
    """
    factory of center
    """

    def __init__(bundle_factory):
        """
        initialize center factory by bundle factory
        """

    def __call__(bundle):
        """
        create object which provide token center
        """

