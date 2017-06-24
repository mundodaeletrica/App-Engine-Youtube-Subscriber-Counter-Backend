# -*- coding: utf-8 -*-
# Copyright 2016 Google Inc.
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

# Modified by Alex Benfica. 
# Used to create a video for Youtube channel Mundo da Eletrica.
# this is the backend for this project using ESP8266 SoC Wifi Module
# https://github.com/mundodaeletrica/WiFi-Youtube-Subscriber-Counter-ESP8266


import webapp2
import os
import urllib
import webapp2
from youtube import getSubscriberCount

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        
        # get channelId parameter
        moduleId = self.request.get('moduleId')
        f = self.request.get('f')        
                
        if f == 'yt':        
            
            #default for Mundo da Eletrica
            channelId = ''
            if moduleId=='MEL100k':
                channelId = 'UCQzm6RcaOty8QU2VhHbRg-g'
                
            # retrieve the number of subscribers        
            if not channelId:
                self.response.write('No id!')
                return

            subsCount = getSubscriberCount(channelId)        
            if subsCount:                        
                subsCount = float(subsCount)

                if subsCount < 1000000:                        
                    subsCount = int(subsCount)
                    self.response.write("%d" % subsCount)                
                    return

                if subsCount > 10000000: #10M
                    self.response.write("%.2fM" % (subsCount / 1000000.0))
                    return

                if subsCount >= 1000000: #1M                                      
                    self.response.write("%.3fM" % (subsCount / 1000000.0))
                    return            

            self.response.write('??????')                
            return        
    
             



app = webapp2.WSGIApplication([
        ('/', MainPage),    
    ], debug=True)
