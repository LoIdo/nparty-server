import collections
import datetime
import hashlib
import json
import urllib2

import zope.interface
import zope.component

import interface.technical.mobile
import interface.technical.configuration


class Mobile(object):
    """
    center of ucpass mobile
    """

    zope.interface.implements(interface.technical.mobile.IMobile)

    def __init__(self):
        config = zope.component.getUtility(
            interface.technical.configuration)
        self.args = {
            'url': config.getValue("ucpaas;sms_url") or "https://api.ucpaas.com/2014-06-30",
            'template': config.getValue("ucpaas;sms_template") or "6848",
            'appid': config.getValue("ucpaas;appid") or "aa9bc12a81964137abde104c230a3a10",
            'sid': config.getValue("ucpaas;sid") or "4117897e587058ec76b4b28f88a28f70",
            'token': config.getValue("ucpaas;token") or "6c9ea33b12ea589a17c1577aeaad886c",
        }

    def sendSMS(self, number, content):
        """ implementation of sendSMS """
        number = str(number)
        ''' use default template '''
        template = self.args.get('template')
        sid = self.args.get('sid')
        stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        sign = hashlib.md5('%s%s%s' % (sid, self.args.get('token'), stamp)).hexdigest().upper()
        url = self.args.get('url') + "/Accounts/%s/Messages/templateSMS?sig=%s" % (sid, sign)
        auth = (sid + ':' + stamp).encode("base64").strip()
        req = urllib2.Request(url)

        ''' setup http body as json '''
        content_list = []
        if (not isinstance(content, basestring))\
                and isinstance(content, collections.Iterable):
            for c in content:
                if isinstance(c, basestring):
                    content_list.append(c)
                elif isinstance(c, int):
                    template = c
            content = ','.join(content_list)
        body = "{'templateSMS':" \
               "{'to':'%s'," \
               "'templateId':'%s'," \
               "'appId':'%s'," \
               "'param':'%s'}}"\
               % (number, template, self.args.get('appid'), content)
        req.add_header("Accept", "application/json")
        req.add_header("Content-Type", "application/json;charset=utf-8")
        req.add_header("Authorization", auth)
        req.add_data(body)
        ''' post request '''
        res = urllib2.urlopen(req).read()
        ''' read response as json '''
        res = json.loads(res)
        if res:
            res = res.get('resp')
            return int(res.get('respCode'))
        return 0

    def sendVoice(self, number, content):
        return NotImplemented