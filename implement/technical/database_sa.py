import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.orm
import zope.interface
import zope.component

import interface.technical.database
import interface.technical.storage


class Operator(sqlalchemy.orm.Session):
    """
    implementation of SQLAlchemy operator
    """
    zope.interface.implements(interface.technical.database.IOperator)

    def __del__(self):
        """ commit transactions """
        try:
            self.commit()
        except sqlalchemy.exc.DatabaseError:
            self.rollback()
            raise
        except sqlalchemy.exc.InvalidRequestError:
            ''' return immediately if there is nothing to commit '''
            pass


class Client(object):
    """
    implementation of SQLAlchemy client
    """
    zope.interface.implements(interface.technical.database.IClient)

    def __init__(self):
        """
        initialize SQLAlchemy by configuration
        """
        config = zope.component.getUtility(
            interface.technical.storage.IStorage)
        self.engine = sqlalchemy.create_engine(
            config.getValue('sqlalchemy;conn')
            or "mysql://root:2v0eps4o@127.0.0.1:3306/nparty?charset=utf8",
            echo=config.getValue('sqlalchemy;debug') or False,
            pool_size=2, pool_recycle=3600)
        self.session_maker = sqlalchemy.orm.scoped_session(
            sqlalchemy.orm.sessionmaker(
                bind=self.engine, class_=Operator, autocommit=True))

    @zope.interface.implementer(interface.technical.database.IOperator)
    def getOperator(self):
        """
        create and return db operator
        """
        op = self.session_maker()
        op.begin(subtransactions=True)
        return op