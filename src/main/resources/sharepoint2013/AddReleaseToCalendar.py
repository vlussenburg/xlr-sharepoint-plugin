#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from sharepoint2013.SharepointClient import SharepointClient
from java.text import SimpleDateFormat
from java.util import TimeZone, Locale, Calendar

iso8601DateFormatter = SimpleDateFormat("yyyy-MM-dd'T'HH:mm'Z'", Locale.ENGLISH)
iso8601DateFormatter.setTimeZone(TimeZone.getTimeZone("UTC"))

if not server:
    raise Exception("Server must be provided")
if not calendarName:
    raise Exception("calendarName must be provided")

def java_date_to_iso8601(java_date):
    return iso8601DateFormatter.format(java_date)

current_release = getCurrentRelease()

client = SharepointClient.create_client(server)
client.connect()

start_date = java_date_to_iso8601(current_release['startDate'])
end_date = java_date_to_iso8601(current_release['dueDate'])

event = {
    "calendar_name" : calendarName, 
    "title" : current_release['title'],
    "start_date" : start_date, 
    "end_date" : end_date, 
    "description" : current_release['description']
}

guid = client.add_calendar_event(event)

print "Calendar event with guid [%s] created." % guid
