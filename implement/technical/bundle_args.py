import argparse
import copy
import os

import zope.interface.declarations
import sqlalchemy
import sqlalchemy.orm

import interface.technical.bundle
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
        self.other = factory.other
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
    other = implement.technical.Dummy()

    def __init__(self, **kwargs):
        """ initialize bundle factory """
        ''' parse arguments '''
        parser = argparse.ArgumentParser()
        parser.add_argument("--conf_file", default=os.path.join(os.path.curdir, "nparty.ini"))
        parser.add_argument('--module_dir', default=os.path.join(os.path.pardir, "shared"))
        parser.add_argument('--port', type=int, default=8888)
        parser.add_argument('--debug', nargs="?", default=argparse.SUPPRESS)
        parser.add_argument('--sal_conn', default="")
        # parser.add_argument('--oss_conn', default="")
        # parser.add_argument('--red_conn', default="")
        args = parser.parse_args()

        ''' create sub component '''
        self.component.technical = implement.technical.Dummy()
        self.component.extension = implement.technical.Dummy()

        ''' set options '''
        self.option.debug = hasattr(args, 'debug')
        ''' set other information '''
        self.other.conf_file = os.path.abspath(args.conf_file)
        self.other.module_dir = os.path.abspath(args.module_dir)
        self.other.port = args.port

        ''' get sqlalchemy configuration string '''
        if args.sal_conn:
            ''' initialize database '''
            self.dependent.sa = implement.technical.Dummy()
            self.dependent.sa.engine = sqlalchemy.create_engine(
                args.sal_conn, echo=self.option.debug, pool_size=2, pool_recycle=3600)
            self.dependent.sa.session_maker = sqlalchemy.orm.scoped_session(
                sqlalchemy.orm.sessionmaker(bind=self.dependent.sa.engine, autocommit=True))

    def __call__(self, **kwargs):
        return _Bundle(self)
