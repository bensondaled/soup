import pyqtgraph as pg

def playmov(mov, rate):
    im = pg.image(mov)
    im.fps = rate
    im.play()
    pg.QtGui.QApplication.exec_()
    try:
        pg.exit()
    except:
        pass

