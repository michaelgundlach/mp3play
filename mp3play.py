import random
import time
from ctypes import windll, c_buffer

class _mci:
    def __init__(self):
        self.w32mci = windll.winmm.mciSendStringA
        self.w32mcierror = windll.winmm.mciGetErrorStringA

    def send(self, command):
        buffer = c_buffer(255)
        errorcode = self.w32mci(str(command), buffer, 254, 0)
        if errorcode:
            return errorcode, self.get_error(errorcode)
        else:
            return errorcode, buffer.value

    def get_error(self, error):
        error = int(error)
        buffer = c_buffer(255)
        self.w32mcierror(error, buffer, 254)
        return buffer.value

    def directsend(self, txt):
        (err, buf) = self.send(txt)
        if err != 0:
            print 'Error %s for "%s": %s' % (str(err), txt, buf)
        return (err, buf)

# TODO: detect errors in all mci calls
class Mp3(object):
    def __init__(self, filename):
        self.filename = filename
        self._alias = 'mp3_%s' % str(random.random())

        self._mci = _mci()

        self._mci.directsend(r'open "%s" alias %s' % (filename, self._alias ))
        self._mci.directsend('set %s time format milliseconds' % self._alias)

        err,buf=self._mci.directsend('status %s length ' % self._alias)
        self._length_ms = int(buf)

    def play(self, start_ms=None, end_ms=None):
        start_ms = 0 if not start_ms else start_ms
        end_ms = self.milliseconds() if not end_ms else end_ms
        err,buf=self._mci.directsend('play %s from %d to %d'
                % (self._alias, start_ms, end_ms) )

    def stop(self):
        self._mci.directsend('stop %s' % self._alias)

    def seconds(self):
        return int(round(float(self.milliseconds()) / 1000))

    def milliseconds(self):
        return self._length_ms

    # TODO: this closes the file even if we're still playing.
    # no good.  detect isplaying(), and don't die till then!
    def __del__(self):
        self._mci.directsend('close %s' % self._alias)
