import numpy as np
import os, h5py
import pandas as pd
import warnings
import pyfluo as pf
import cv2
cv2.ocl.setUseOpenCL(False)
from skimage.io import imread,imsave
from .funcs import x, savefig, loadfig, tic, toc, norm
from .mpl import *
from .colormaps import *
from .images import *
from .animation import Animation
from .shapes import *
from .audio import play
from .movies import playmov
from .math import mode

#warnings.filterwarnings('ignore', "tight_layout : falling back to Agg renderer")
pd.options.mode.chained_assignment = None
