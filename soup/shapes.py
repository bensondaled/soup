import cv2, numpy as np

def pts_to_mask(pts, shape):
    """
    Pts in (x,y)
    """
    pts = np.round(pts).astype(int)
    mask = np.zeros(shape, dtype=np.int32)
    cv2.fillConvexPoly(mask, pts, (1,1,1), lineType=cv2.LINE_AA)
    return mask
