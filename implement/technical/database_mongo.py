import pymongo
import zope.interface
import zope.component

import interface.technical.database
import interface.technical.configuration


'''
class Operator(object):
    """
    implements for operation
    """
    zope.interface.implements(interface.technical.database.IOperator)

    def __init__(self):
        pass

    def __del__(self):
        """
        :return:
        """
'''


class Client(object):
    """
    implements for mongodb client
    """
    zope.interface.implements(interface.technical.database.IClient)

    def __init__(self):
        """
        initialize mongodb by configuration
        """
        config = zope.component.getUtility(
            interface.technical.configuration)
        mongo_url = config.getValue('mongodb;conn')\
            or 'mongodb://root:2v0eps4o@ushouhou.cn/nparty'
        self.engine = pymongo.MongoClient(mongo_url)
        self.engine = self.engine[mongo_url.rsplit('/', 1)[1]]
        zope.interface.directlyProvides(
            self.engine, interface.technical.database.IOperator)

    def getOperator(self):
        return self.engine