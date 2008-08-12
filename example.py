import mp3play

file = mp3play._f
mp3 = mp3play.Mp3(file)

mp3.play()

# Let it play for up to 30 seconds, then stop it.
import time
time.sleep(min(5, mp3.seconds()))
mp3.stop()
