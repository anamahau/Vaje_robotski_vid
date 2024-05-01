import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as im
from scipy.interpolate import interpn

# Nalozi sliko
def loadImage(iPath):
    oImage = np.array(im.open(iPath))
    return oImage

# Prikazi sliko
def showImage(iImage, iTitle=''):
    plt.figure()
    plt.imshow(iImage, cmap = 'gray')
    plt.suptitle(iTitle)
    plt.xlabel('x')
    plt.ylabel('y')
    
# Pretvori v sivinsko sliko
def colorToGray(iImage):
    dtype = iImage.dtype
    r = iImage[:,:,0].astype('float')
    g = iImage[:,:,1].astype('float')
    b = iImage[:,:,2].astype('float')
    
    return (r*0.299 + g*0.587 + b*0.114).astype(dtype)

def addHomCoord2D(iPts):
    if iPts.shape[-1] == 3:
        return iPts
    iPts = np.hstack((iPts, np.ones((iPts.shape[0], 1))))
    return iPts

def transProjective2D(iPar, iCoorX, iCoorY):
    """Funkcija za projektivno preslikavo"""
    iPar = np.asarray(iPar)
    iCoorX = np.asarray(iCoorX)
    iCoorY = np.asarray(iCoorY)
    if np.size(iCoorY) != np.size(iCoorX):
        print("Stevilo X in Y koordinat razlicno!")
    # iPar = [a11, a12, tx, a21, a22, ty, px, py]
    oDenom = iPar[6] * iCoorX + iPar[7] * iCoorY + 1
    oCoorU = iPar[0] * iCoorX + iPar[1] * iCoorY + iPar[2]
    oCoorV = iPar[3] * iCoorX + iPar[4] * iCoorY + iPar[5]
    return oCoorU/oDenom, oCoorV/oDenom

def geomCalibImage(iPar, iImage, iCoorX, iCoorY):
    """Funkcija za normalizacijo slike po geometrijski kalibraciji"""
    oCoorUt, oCoorVt = transProjective2D(iPar, iCoorX, iCoorY)
    dy = iImage.shape[0]
    dx = iImage.shape[1]
    s = 1
    oImage = interpn((np.arange(dy), np.arange(dx)),
                      iImage,
                      (oCoorVt[::s,::s], oCoorUt[::s,::s]),
                      method = "linear", bounds_error=False)
    return oImage

def getPoints(img, calib=False):
    if calib:
        img_g = colorToGray(img)
        iCoorX, iCoorY = np.meshgrid(range(img_g.shape[1]), 
                                    range(img_g.shape[0]),
                                    sparse=False, indexing='xy')
        iPar = [4.452, -0.349, 34.207, -0.709,
                3.352, 211.927, 2.459e-04, -1.348e-03,
                1963.270, 1478.125, 1.101e-03]
        iCoorX = iCoorX / 3
        iCoorY = iCoorY / 3
        img = geomCalibImage(iPar, img_g, iCoorX, iCoorY)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')

    points = []
    def onclick(event):
        if event.key == 'shift':
            x, y = event.xdata, event.ydata
            points.append((x, y))
            ax.plot(x, y, 'or')
            fig.canvas.draw()
    
    ka = fig.canvas.mpl_connect('button_press_event', onclick)

    # VRSTNI RED POMEMBEN KLIKAMO (SHIFT+klik) V SMERI URINEGA KAZALCA

    plt.show()
    print(points)

if __name__ == '__main__':

    getPoints(loadImage('./data/calibration-object.jpg'))
    #getPoints(loadImage('./data/test-object.jpg'), calib=True)