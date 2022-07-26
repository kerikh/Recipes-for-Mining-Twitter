# -*- coding: utf-8 -*-

import os
import sys
import datetime
import time
import json
import twitter

t = twitter.Twitter(domain='api.twitter.com', api_version='1')

if not os.path.isdir('out/trends_data'):
        os.makedirs('out/trends_data')

while True:

        now = str(datetime.datetime.now())

        trends = json.dumps(t.trends._(1)(), indent=1)

        with open(os.path.join(os.getcwd(), 'out', 'trends_data', now), 'w') as f:
                f.write(trends)
        now = str(datetime.datetime.now())

        now = str(datetime.datetime.now())

        time.sleep(60) # 60 seconds
