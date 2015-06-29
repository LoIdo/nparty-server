import sqlalchemy.exc
import zope.interface.declarations

import interface.technical.transaction


@zope.interface.declarations.implementer(interface.technical.transaction.ITransaction)
@zope.interface.declarations.provider(interface.technical.transaction.ITransactionFactory)
class _Transaction(object):
    """
    transaction for SQLAlchemy
    """

    def __init__(self, session):
        self.session = session

    def __enter__(self):
        """
        begin transaction
        """
        self.session.begin(subtransactions=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        end transaction
        """
        if exc_type is not None:
            return False
        ''' commit transactions '''
        try:
            self.session.commit()
        except sqlalchemy.exc.DatabaseError:
            self.session.rollback()
            raise
        except sqlalchemy.exc.InvalidRequestError:
            ''' return immediately if there is nothing to commit '''
            pass


@zope.interface.declarations.implementer(interface.technical.transaction.ITransactionFactory)
class Factory(object):
    """
    factory of customer center interface
    """
    def __init__(self, bundle_factory):
        """  initialize transaction factory """

    def __call__(self, bundle):
        """ create object provide interface """
        return _Transaction(bundle.dependent.sa.session)
