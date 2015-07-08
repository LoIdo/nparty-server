import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import zope.interface.declarations

import interface.technical.configuration


class _Table(sqlalchemy.ext.declarative.declarative_base()):
    """
    table for login
    """
    ''' table name '''
    __tablename__ = 'us_config'
    ''' configuration key '''
    key = sqlalchemy.Column(sqlalchemy.String(64), nullable=False, primary_key=True)
    ''' configuration value '''
    value = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)


@zope.interface.declarations.implementer(interface.technical.configuration.IConfig)
@zope.interface.declarations.provider(interface.technical.configuration.IConfigFactory)
class _Config(object):
    """
    class implements authentication center interface
    """
    
    def __init__(self, engine, cache):
        """ init all variables """
        ''' initialize configuration cache '''
        self.cache = cache
        ''' initialize Sqlalchemy session '''
        self.session = sqlalchemy.orm.scoped_session(
            sqlalchemy.orm.sessionmaker(bind=engine, autocommit=True))()
    
    def set_value(self, key, value):
        self.session.begin(subtransactions=True)
        try:
            self.session.merge(_Table(key=key, value=value))
            self.session.commit()
            ''' store to cache '''
            self.cache[key] = value
            return True
        except sqlalchemy.exc.DatabaseError:
            self.session.rollback()
        return False

    def get_value(self, key):
        try:
            ''' find in cache first '''
            return self.cache[key]
        except KeyError:
            pass
        val = self.session.query(_Table.value)\
            .filter(_Table.key == key).first()
        if val:
            val = val[0]
            ''' store to cache  '''
            self.cache[key] = val
            return val

    def update_values(self):
        """ clean all values in cache """
        self.cache.clear()


class Factory(object):
    """
    factory of register center interface
    """

    def __init__(self, bundle_factory):
        _Table.metadata.create_all(bundle_factory.dependent.sa.engine)
        self.cache = dict()

    def __call__(self, bundle):
        """ create object provide interface """
        return _Config(bundle.dependent.sa.engine, self.cache)
