#!/usr/bin/python

import traceback
import time

CHECK_GIT_FOR_UPDATES_EVERY = 30


print "Starting up..."
while True:
    try:
        print "!"
        time.sleep(20)
    except Exception, ex:
        traceback.print_exc()
        continue
