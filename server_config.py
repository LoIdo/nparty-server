import tornado.wsgi
import zope.configuration.xmlconfig

""" load ZCML file """
zope.configuration.xmlconfig.file('server_config.zcml')
application = tornado.wsgi.WSGIApplication()
