import zope.interface


class ICenter(zope.interface.Interface):
    """
    center of access token
    """

    def addToken(value, timeout):
        """
        generate access token by value
        same value mapping to only one token
        return token id
        """

    def rmvToken(token_id):
        """
        remove access token by id
        """

    def rmvTokenMatch(token_id, value):
        """
        remove access token by id
        and while value is match
        """

    def chkToken(token_id):
        """
        check value of token
        """