# Copyright 2016 Google Inc. All rights reserved.
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
# See the License for the specific language governing permissions and
# limitations under the License.

from google.appengine.api import urlfetch
import json
import api_key


def getSubscriberCount(channelId):

    # youtube V3 API key
    API_KEY = 'AIzaSyBwdWB55h3mZUQeHiURIv8fjMK7vB5SccE';

    # https://developers.google.com/youtube/v3/docs/channels/list#try-it
    url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=%s&key=%s' % (channelId, YOUTUBE_DATA_API_KEY)

    r = urlfetch.fetch(url)
    if r.status_code == 200:
        try:
            items = json.loads(r.content)['items'][0]
            subsCount = items.get('statistics',{}).get('subscriberCount',0)
            return subsCount
        except:
            return 0
    else:
        return 0


#print getSubscriberCount('UCQzm6RcaOty8QU2VhHbRg-g')
