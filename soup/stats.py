import numpy as np

def cohensd(x1, x2):
    """
    https://en.wikipedia.org/wiki/Effect_size#Cohen.27s_d
    """
    nx1 = len(x1)
    nx2 = len(x2)
    dof = nx1 + nx2 - 2 # -2 is optional, dependent on source
    return (np.mean(x1) - np.mean(x2)) / np.sqrt( ((nx1-1)*np.std(x1, ddof=1) ** 2 + (nx2-1)*np.std(x2, ddof=1) ** 2) / dof )

