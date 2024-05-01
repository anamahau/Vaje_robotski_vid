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

# Nalozimo in prikazemo slike
iCalImage = loadImage('D:/Izobrazevanje/4_FE_UNI_LJ/4._letnik/2. semester/Robotski vid/Laboratorijske vaje/06_Geometrijska_kalibracija_kamere/06_geometrijska_kalibracija_kamere/data/calibration-object.jpg')
#iCalImage = loadImage('D:/Izobrazevanje/4_FE_UNI_LJ/4._letnik/2. semester/Robotski vid/Laboratorijske vaje/06_geometrijska_kalibracija_kamere/06_geometrijska_kalibracija_kamere/data/test-object.jpg')
iCalImage = loadImage('D:/Izobrazevanje/4_FE_UNI_LJ/4._letnik/2. semester/Robotski vid/Laboratorijske vaje/06_geometrijska_kalibracija_kamere/06_geometrijska_kalibracija_kamere/data/kalibrirana_slika.png')

# Testirajte funkcijo geomCalibErr
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(colorToGray(iCalImage), cmap='gray')

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

'''
[(116.61693548387095, 266.0322580645163), (645.2258064516128, 171.07258064516145), (1139.0161290322578, 82.44354838709683), (1243.4717741935483, 386.3145161290323), (1370.0846774193546, 762.9879032258066), (752.8467741935483, 902.2620967741937), (81.79838709677418, 1047.8669354838712), (100.79032258064515, 607.8870967741937)]
'''