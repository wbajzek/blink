#!/usr/local/Cellar/python/2.7.5/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python

# this is derived from https://github.com/arvydas/blinkstick-python
#
# use it like this:
#   blink.py <some command>
# and it will pulse your blinkstick until that command is done, then light it red
# or green depending on the outcome.
#
# I chmod it to +x, symlink it to my bin/ directory and use it to show me the status
# of my main work project's automated tests, which take several minutes to run.
# That way I can keep an eye on it while I'm playing foosball.

from blinkstick import blinkstick
import sys
import threading
import os

def heartbeat(stick):
    global done
    intensity = 0
    up = True
    scale = 1
    limit = 255 * scale

    try:
      while not done:
        stick.set_color(intensity/scale, intensity/scale, intensity/scale)
        if up:
          if intensity < limit:
            intensity = intensity + 1
          else:
            up = False
        else:
          if intensity > 0:
            intensity = intensity - 1
          else:
            up = True
    except KeyboardInterrupt as e:
      stick.set_color(0,0,0)
      exit(0)



def main():
    global sticks
    global done


    sticks = blinkstick.find_all()

    for stick in sticks:

        command = sys.argv
        command.pop(0)
        command = ' '.join(command)

        try:
          done = False
          pulse = threading.Thread(target=heartbeat, args=(sticks[0],))
          pulse.start()
          status = os.system(command)
          done = True
          if status == 0:
            stick.set_color(0,127,0)
          else:
            stick.set_color(127,0,0)
          print "Press enter to finish"
          raw_input()
          stick.set_color(0,0,0)

        except Exception as e:
          print e
          print "Unable to run heartbeat"


    return 0


if __name__ == "__main__":
    sys.exit(main())
