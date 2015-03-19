If you have any trouble with the examples below, please [leave a comment](Discussion.md) about it, and I or another user will be glad to help you out.

## Quick reference ##

`mp3play.load(filename)` or `mp3play.AudioClip(filename)` gives an `AudioClip` representing the file.

`AudioClip` methods:

  * `play()`: Start playing the clip.  Returns immediately.
  * `stop()`: Stop playing the clip if it was playing.
  * `pause()`, `unpause()`: Pause (if playing) or unpause (if paused).
  * `isplaying()`: True if the clip is currently playing and not paused.
  * `ispaused()`: True if the clip is currently paused.
  * `seconds()`: The duration of the clip in seconds, rounded to the nearest second.
  * `milliseconds()`: The duration of the clip in milliseconds.

## Simplest example ##

Play an MP3 for 30 seconds.

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