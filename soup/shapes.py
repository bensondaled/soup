try:
    import cv2
except:
    cv2 = None
import numpy as np

def pts_to_mask(pts, shape):
    """
    Pts in (x,y)
    """
    if cv2 is None:
        return
    pts = np.round(pts).astype(int)
    mask = np.zeros(shape, dtype=np.int32)
    cv2.fillConvexPoly(mask, pts, (1,1,1), lineType=cv2.LINE_AA)
    return mask
