import zope.interface


class ITransaction(zope.interface.Interface):
    """
    abstract transaction logic
    """

    def begin():
        """
        begin transaction
        """

    def end():
        """
        exit code block
        end transaction
        """