import sys
''' set default encoding to utf8  '''
reload(sys)
sys.setdefaultencoding('utf-8')

import implement.technical.bundle_args
import implement.technical.bundle_conf
import implement.technical.configuration_cp

''' create bundle factory to initialize server '''
_bundle_factory = implement.technical.bundle_args.Factory()
if _bundle_factory.other.conf_file:
    ''' overwrite bundle factory '''
    _bundle_factory = implement.technical.bundle_conf.Factory(
        config=implement.technical.configuration_cp.Factory(
            _bundle_factory)(_bundle_factory()))

''' add specified modules root path '''
if _bundle_factory.other.module_dir not in sys.path:
    sys.path.insert(0, _bundle_factory.other.module_dir)


def run(handler):
    """  service run """
    ''' install handler of main logic '''
    app = handler(_bundle_factory)

    try:
        ''' try gevent first '''
        import gevent.monkey
        import gevent.wsgi
        ''' patch all io method '''
        gevent.monkey.patch_all()
        server = gevent.wsgi.WSGIServer(
            ('', _bundle_factory.other.port), app)
        server.serve_forever()  # start gevent WSGI
    except ImportError:
        import tornado.httpserver
        import tornado.ioloop
        import tornado.wsgi
        server = tornado.httpserver.HTTPServer(
            tornado.wsgi.WSGIContainer(app))
        server.listen(_bundle_factory.other.port)
        tornado.ioloop.IOLoop.instance().start()  # start tornado IOLoop