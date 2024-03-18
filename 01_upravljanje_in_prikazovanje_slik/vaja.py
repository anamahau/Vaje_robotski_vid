from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def showImage(image, iTitle='Slika'):
    plt.figure()
    plt.imshow(image, cmap='gray') #cmap = barvna skala prikaza 2D slike
    plt.title(iTitle)
    plt.show()

def loadImageRaw(iPath, iSize, iFormat):
    raw_image_vector = np.fromfile(iPath, dtype=iFormat)
    oImage = raw_image_vector.reshape(iSize)
    return oImage

def saveImageRaw(iImage, iPath, iFormat):
    #iImage je numpy slika
    iImage = iImage.flatten().astype(iFormat) #matriko spremeni nazaj v vektor
    iImage.tofile(iPath)

def showImageRGB(image, iTitle='Slika'):
    #showImage za RGB sliko
    plt.figure()
    plt.imshow(image)
    plt.title(iTitle)
    plt.show()

def loadImageRawRGB(iPath, iSize, iFormat):
    #loadImageRaw za RGB sliko
    raw_image_vector = np.fromfile(iPath, dtype=iFormat)
    oImage = raw_image_vector.reshape(iSize)
    return oImage

def saveImageRawRGB(iImage, iPath, iFormat):
    #saveImageRaw za RGB sliko
    iImage = iImage.flatten().astype(iFormat)
    iImage.tofile(iPath)

if __name__ == '__main__':
    img = Image.open('01_upravljanje_in_prikazovanje_slik\data\slika.jpg')

    #plt.figure()
    #plt.imshow(img)
    #plt.show()

    #ali je slika res zapisana kot RGB?
    print('Preveri, v katerem formatu je slika:', img.getbands())

    #pretvori sliko v crno-belo
    img_gray = img.convert('L')
    #plt.figure()
    #plt.imshow(img_gray)
    #plt.show() #kva?
    print(np.shape(img_gray))
    #plt.figure()
    #plt.imshow(img_gray, cmap='gray') #cmap = barvna skala prikaza 2D slike
    #plt.show() #mnogo bolje, slika dejansko je crno-bela, fascinantno

    img_array = np.array(img)
    for i in range(np.shape(img_array)[2]):
        #showImage(img_array[:,:,i])
        pass

    #djmo se shrant sliko (za foro sm rdeco komponento, da mal zakompliciramo)
    img_r = img_array[:,:,0] #0...R, 1...G, 2...B
    img_new = Image.fromarray(img_r)
    #img_new.save('01_upravljanje_in_prikazovanje_slik/data/new_image.png')

    raw_image_vector = np.fromfile('01_upravljanje_in_prikazovanje_slik/data/slika-8bit.raw', dtype='uint8')
    print(raw_image_vector)
    raw_image_matrix = raw_image_vector.reshape([650, 975])
    showImage(raw_image_matrix)

    image_raw = loadImageRaw('01_upravljanje_in_prikazovanje_slik/data/slika-8bit.raw', [650, 975], 'uint8')
    showImage(image_raw, iTitle='8 bitna raw slika')

    #saveImageRaw(image_raw, '01_upravljanje_in_prikazovanje_slik/data/new_raw.png', 'uint16')

    image_raw_16bit = loadImageRaw('01_upravljanje_in_prikazovanje_slik/data/new_raw.png', [650, 975], 'uint16')
    showImage(image_raw_16bit, iTitle='16 bitna raw slika')


    image_new_rgb = loadImageRawRGB('01_upravljanje_in_prikazovanje_slik\data\slika-24bit-rgb.raw', [650, 975, 3], 'uint8')
    showImageRGB(image_new_rgb, iTitle='RGB raw slika')