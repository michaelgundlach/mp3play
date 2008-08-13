import mp3play

clip = mp3play.load(r'C:\music.mp3')

clip.play()

# Let it play for up to 30 seconds, then stop it.
import time
time.sleep(min(5, clip.seconds()))
clip.stop()
