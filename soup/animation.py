import matplotlib.pyplot as pl
from subprocess import call
import os

class Animation():
    def __init__(self, base, fig=None, interval=1.):
        self.path = base
        self.fig = fig or pl.gcf()
        self.interval = interval

        self._tmpname = self.path + '_tmp{:05d}.png'
        self._idx = 0
        self._tmplist = []
       
    def put(self):
        savename = self._tmpname.format(self._idx)
        pl.savefig(savename)
        self._tmplist.append(savename)
        self._idx += 1

    def end(self):
        call(['ffmpeg', '-f', 'image2', '-r', '1/{}'.format(int(self.interval)), '-i', '{}_tmp%05d.png'.format(self.path), '-vcodec', 'mpeg4', '-y', self.path+'.mp4'])
        for n in self._tmplist:
            os.remove(n)
