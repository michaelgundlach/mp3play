# mp3play #

mp3play is a Python package that provides a simple interface for playing music from an MP3 file.  No other modules or installations are required -- it Just Works.  It's very easy to use within a program that needs to play all or part of an MP3 without opening an external player.

It is available on PyPI at http://pypi.python.org/pypi/mp3play/ .

**Questions?**  You can contact Michael Gundlach, the developer, at gundlach at gmail.  Or, just file a bug under "Issues" above.


## Requirements: ##

Windows XP at the moment, but the goal is to make cross-platform.  I'd love patches that made this run seamlessly under Linux and Mac: please send in a patch!

## Installation: ##

Type `easy_install mp3play` at the Windows command prompt.  (If that doesn't work, download and run [this Python script](http://peak.telecommunity.com/dist/ez_setup.py) to install easy\_install, then try again from C:\<Your python directory>\Scripts\ .)

## Example code ##

```
import mp3play

filename = r'C:\Documents and Settings\Michael\Desktop\music.mp3'
mp3 = mp3play.load(filename)

mp3.play()

# Let it play for up to 30 seconds, then stop it.
import time
time.sleep(min(30, mp3.seconds()))
mp3.stop()
```

More complex examples are available [here](Examples.md).

## Thanks ##

To Michel Claveau for his original code on which the Windows guts of mp3play are based.