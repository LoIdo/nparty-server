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


class ITransactionFactory(zope.interface.Interface):
    """
    transaction center interface factory
    """

    def __init__(bundle_factory):
        """
        initialize transaction factory
        """

    def __call__(bundle):
        """
        create an object which provide transaction interface
        """
