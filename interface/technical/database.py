import zope.interface


class IOperator(zope.interface.Interface):
    """
    transaction of database
    """


class IClient(zope.interface.Interface):
    """
    client connection to database server
    """

    def getOperator():
        """
        get an operator of database
        """