#!/usr/bin/python

import traceback
import time
import subprocess
import os.path

CHECK_GIT_FOR_UPDATES_EVERY_MINUTES = 1

update_git_timer = 0

SAY_VOICE = "Alex"

def do_say(saying, voice=SAY_VOICE):
    subprocess.call(['say', '-v', voice, saying)

do_say("Starting up...", voice="Trinoids")
while True:
    try:
        now = time.time()
        if (now - (CHECK_GIT_FOR_UPDATES_EVERY_MINUTES*60)) > update_git_timer:
            print "Checking for updates..."
            if os.path.exists('../updater.sh'):
                subprocess.check_call(["../updater.sh"])
            else:
                print "Can't check for updates, no updater.sh :("
        print "!"
        time.sleep(20)
    except subprocess.CalledProcessError:
        print "TERMINATING DUE TO CalledProcessError!"
        import sys
        sys.exit(0)
    except Exception, ex:
        traceback.print_exc()
        continue
