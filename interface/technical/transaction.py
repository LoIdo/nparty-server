import zope.interface


class ITransaction(zope.interface.Interface):
    """
    abstract transaction logic
    """

    def __enter__():
        """
        enter code block
        begin transaction
        """

    def __exit__(exc_type, exc_val, exc_tb):
        """
        exit code block
        end transaction
        """