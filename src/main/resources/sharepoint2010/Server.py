#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from sharepoint2010.HttpRequest import HttpRequest
import com.xhaus.jyson.JysonCodec as json

contentType = 'application/json'
headers = {'Accept' : 'application/json'}

# get the configuration properties from the UI
params = {  'url': configuration.url, 
            'username' : configuration.username, 
            'password': configuration.password,  
            'proxyHost': configuration.proxyHost, 
            'proxyPort': configuration.proxyPort, 
            'proxyUsername': configuration.proxyUsername, 
            'proxyPassword': configuration.proxyPassword, 
            'domain': configuration.domain, 
            'authenticationMethod': configuration.authenticationMethod 
        }

# do an http request to the server
response = HttpRequest(params).get('/_vti_bin/ListData.svc/Calendar', contentType = 'application/json', headers=headers)

# check response status code, if is different than 200 exit with error code
if response.status != 200:
    logger.error("Couldn't establish the connection with server.", response)

responseJson = json.loads(response.response)
logger.info(str(responseJson))



