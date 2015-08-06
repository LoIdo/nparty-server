import sqlalchemy
import sqlalchemy.exc
import zope.interface
import zope.component

import interface.technical.transaction


class Transaction(object):
    """
    transaction for SQLAlchemy
    """
    zope.interface.implements(interface.technical.transaction.ITransaction)

    def __init__(self, session):
        self.session = session

    def begin(self):
        """
        begin transaction
        """
        self.session.begin(subtransactions=True)
        return self

    def end(self):
        """
        end transaction
        """
        ''' commit transactions '''
        try:
            self.session.commit()
        except sqlalchemy.exc.DatabaseError:
            self.session.rollback()
            raise
        except sqlalchemy.exc.InvalidRequestError:
            ''' return immediately if there is nothing to commit '''
            pass