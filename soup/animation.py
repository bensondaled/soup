import matplotlib.pyplot as pl
from subprocess import call
import os

class Animation():
    def __init__(self, base, fig=None, rate=1., dpi=100, codec='mpeg4'):
        self.path = base
        self.fig = fig or pl.gcf()
        self.rate = rate
        self.dpi = dpi
        self.codec = codec

        self._tmpname = self.path + '_tmp{:05d}.png'
        self._idx = 0
        self._tmplist = []
       
    def put(self):
        savename = self._tmpname.format(self._idx)
        pl.savefig(savename, dpi=self.dpi)
        self._tmplist.append(savename)
        self._idx += 1

    def end(self):
        call(['ffmpeg', '-f', 'image2', '-r', '{}'.format(int(self.rate)), '-i', '{}_tmp%05d.png'.format(self.path), '-vcodec', self.codec, '-y', self.path+'.mp4'])
        for n in self._tmplist:
            os.remove(n)
