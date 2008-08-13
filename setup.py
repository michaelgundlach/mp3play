from setuptools import setup

setup(name='mp3play',
      version='0.1.6',
      py_modules=['mp3play'],

      description="A simple interface for playing music from an MP3 file.""",
      long_description=r"""
------------
mp3play
------------

  Allows your Windows Python program to play and stop MP3s, without opening
  an external player or requiring any external programs.  A very simple
  interface for the common case (playing an entire MP3), with an API for
  more complex tasks (e.g. playing from seconds 30 to 45 of an MP3).

Example
=======

  Play the first 30 seconds of a file::

    import mp3play

    file = r'C:\Documents and Settings\Michael\Desktop\music.mp3'
    mp3 = mp3play.Mp3(file)

    mp3.play()

    import time
    time.sleep(min(30, mp3.seconds()))
    mp3.stop()

Requirements
============

  Requires Windows XP at the moment, but the goal is to make a
  cross-platform module.  Feel free to send patches to add Linux and
  Mac support!

Resources
=========

  * Homepage: http://mp3play.googlecode.com/
  * Source:

    - Browse at http://code.google.com/p/mp3play/source/browse/trunk/

    - Get with **svn co http://mp3play.googlecode.com/svn/trunk/
      mp3play-read-only**

  Please let me know if you like or use this module - it would make
  my day!
""",

      author='Michael Gundlach',
      author_email='gundlach@gmail.com',
      url='http://code.google.com/p/mp3play/',
      keywords = "mp3 api play music audio python module",

      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Win32 (MS Windows)',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Topic :: Multimedia :: Sound/Audio',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ]

     )
