import tornado.web
import tornado.escape


class CommonHandler(tornado.web.RequestHandler):
    """ common handler for http request """

    @staticmethod
    def input_format(input_string):
        return {} if not input_string\
            else tornado.escape.json_decode(input_string)

    @staticmethod
    def output_format(error_code, **kwargs):
        """ return format error code text """
        fmt = {'error_code': error_code}
        fmt.update(kwargs)
        return fmt

    def initialize(self):
        """ resolve cross domain problem """
        self.set_header("Access-Control-Allow-Origin",
                        self.request.headers.get("Origin") or "*")

    def data_received(self, chunk):
        """  do nothing to receive data """
        pass

    def write_error(self, status_code, **kwargs):
        """ overwrite method to handle exception to log """
        try:
            for e in kwargs["exc_info"]:
                if isinstance(e, tornado.web.HTTPError):
                    pass
                elif isinstance(e, Exception):
                    ''' just print error '''
                    print e
        except KeyError:
            pass


class CommonBundleHandler(CommonHandler):
    """ common handler with bundle """
    ''' bundle used by current handler '''
    bundle = None

    def initialize(self, bundle_factory):
        """ initialize with bundle maker """
        super(CommonBundleHandler, self).initialize()
        ''' create bundle for current request '''
        self.bundle = bundle_factory()

    def get(self, *args, **kwargs):
        """ make the same of GET and POST method when debug """
        if self.bundle.option.debug:
            self.post(*args, **kwargs)