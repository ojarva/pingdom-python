# -*- coding: utf-8 -*-
"""

    pingdom.exception

"""
# Author: Mike Babineau <mikeb@ea2d.com>
# Copyright 2011 Electronic Arts Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License

try:
    from urllib2 import HTTPError
except:
    from urllib.error import HTTPError

try:
    import json
except:
    import simplejson as json

import StringIO
import urllib2
import gzip
import logging
log = logging.getLogger(__name__)

class PingdomError(Exception):

    def __init__(self, http_response):
        """
        """
        content = json.loads(http_response.content)
        self.status_code = http_response.status_code
        self.status_desc = content['error']['statusdesc']
        self.error_message  = content['error']['errormessage']
        super(PingdomError, self).__init__(self.__str__() )

    def __repr__(self):
        return 'PingdomError: HTTP `%s - %s` returned with message, "%s"' % \
               (self.status_code, self.status_desc, self.error_message)

    def __str__(self):
        return self.__repr__()

class PingdomHTTPError(PingdomError, urllib2.HTTPError):
    def __init__(self, http_error):
        urllib2.HTTPError.__init__(self, http_error.filename, http_error.code, http_error.msg, http_error.hdrs, http_error.fp)

        if self.headers.get('content-encoding') == 'gzip':
            data = gzip.GzipFile(fileobj=StringIO.StringIO(http_error.read())).read()
        else:
            data = self.read()

        j = json.loads(data)
        error = j['error']
        self.statuscode = error['statuscode']
        self.statusdesc = error['statusdesc']
        self.errormessage = error['errormessage']

    def __repr__(self):
        return 'PingdomError: HTTP %s %s returned with message, "%s"' % (self.statuscode, self.statusdesc, self.errormessage)



