import sys, pickle, time
import matplotlib.pyplot as pl

def x():
    sys.exit(0)

def savefig(path):
    with open(path, 'wb') as f:
        pickle.dump(pl.gcf(), f)

def loadfig(path):
    with open(path, 'rb') as f:
        pickle.load(f)

def tic():
    global _tic_t0
    _tic_t0 = time.clock()

def toc(label='Process'):
    global _tic_t0
    res = time.clock() - _tic_t0
    print('{} took {:0.4f} seconds'.format(label,res))
    return res
    
def norm(x, **kwargs):
    return (x-x.min(**kwargs))/(x.max(**kwargs)-x.min(**kwargs))
