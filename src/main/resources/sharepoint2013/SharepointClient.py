#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sys
import urllib
import com.xhaus.jyson.JysonCodec as json
from sharepoint2013.HttpRequest import HttpRequest

HTTP_SUCCESS       = 200
HTTP_CREATED       = 201


class SharepointClient(object):
    def __init__(self, httpConnection): 
        self.headers        = {'Accept' : 'application/json;odata=verbose'}
        self.contentType = 'application/json;odata=verbose'
        self.httpConnection = httpConnection
        self.httpRequest = HttpRequest(self.httpConnection)

    @staticmethod
    def create_client(httpConnection):
        return SharepointClient(httpConnection)

    def connect(self):
        # in order to POST anything, we need a X-RequestDigest header populated with a field from this endpoint
        response = self.httpRequest.post('/_api/contextInfo', "{}", contentType = self.contentType, headers=self.headers)

        if response.status != HTTP_SUCCESS:
            sys.exit("Error in connect code [%s] message [%s]." % (response.status, response.response))

        responseJson = json.loads(response.response)
        self.headers['X-RequestDigest'] = responseJson['d']['GetContextWebInformation']['FormDigestValue']

        print "Successfully connect, request token [%s]" % self.headers['X-RequestDigest']


    def add_calendar_event(self, calendar_event):
        calendar_name = calendar_event['calendar_name']
        from datetime import datetime
        calendarItem =  {  
            'EventDate' : calendar_event['start_date'],
            'Description' : calendar_event['description'],
            'Category' : None,
            'Title': calendar_event['title'],
            'EndDate': calendar_event['end_date'],
            '__metadata':{  
                'type': 'SP.Data.%sListItem' % calendar_name,
            }
        }

        response = self.httpRequest.post('/_api/lists/GetByTitle(\'%s\')/items' % calendar_name, json.dumps(calendarItem), contentType = self.contentType, headers=self.headers)

        if response.status != HTTP_CREATED:
            sys.exit("Error in add_calendar_event code [%s] message [%s]." % (response.status, response.response))

        responseJson = json.loads(response.response)

        print "Successfully created calendar event."

        return responseJson['d']['GUID']
