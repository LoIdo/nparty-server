import copy

import zope.interface.declarations
import sqlalchemy
import sqlalchemy.orm

import interface.technical.bundle
import interface.technical.configuration
import implement.technical


@zope.interface.declarations.implementer(interface.technical.bundle.IBundle)
class _Bundle(object):
    """
    implement of IBundle interface
    """

    ''' implement of attributes  '''
    dependent = implement.technical.Dummy()
    component = None
    option = None
    other = None

    def __init__(self, factory):
        """ initialize bundle """
        self.option = factory.option
        self.component = factory.component
        ''' copy every sub attribute of variable dependent '''
        for var in vars(factory.dependent):
            setattr(self.dependent, var, copy.copy(
                getattr(factory.dependent, var)))
        ''' create a new session '''
        self.dependent.sa.session\
            = self.dependent.sa.session_maker()


@zope.interface.declarations.implementer(interface.technical.bundle.IBundleFactory)
@zope.interface.declarations.provider(interface.technical.bundle.IBundle)
class Factory(object):
    """
    implement of bundle factory
    """
    component = implement.technical.Dummy()
    dependent = implement.technical.Dummy()
    option = implement.technical.Dummy()

    def __init__(self, **kwargs):
        config = kwargs.get('config')
        if not interface.technical.configuration.IConfig.providedBy(config):
            raise Exception('bundle should be initialized by config center')

        self.component.technical = implement.technical.Dummy()
        self.component.extension = implement.technical.Dummy()

        ''' check running options '''
        self.option.debug = config.get_value('debug')
        ''' set other information '''
        self.other.conf_file = config.get_value('conf_file')
        self.other.module_dir = config.get_value('module_dir')
        self.other.port = config.get_value('port')

        ''' get sqlalchemy configuration string '''
        sal_conn = config.get_value('sal_conn')
        if sal_conn:
            ''' initialize database '''
            self.dependent.sa = implement.technical.Dummy()
            self.dependent.sa.engine = sqlalchemy.create_engine(
                sal_conn, echo=self.option.debug, pool_size=2, pool_recycle=3600)
            self.dependent.sa.session_maker = sqlalchemy.orm.scoped_session(
                sqlalchemy.orm.sessionmaker(bind=self.dependent.sa.engine, autocommit=True))

    def __call__(self, **kwargs):
        return _Bundle(self)


