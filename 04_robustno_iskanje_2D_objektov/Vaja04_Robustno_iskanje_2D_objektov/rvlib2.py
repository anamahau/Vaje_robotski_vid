import numpy as np

def gammaImage( iImage, iGamma ):
    """Gama preslikava: (Ls-1)(I/(Lr-1))^gamma"""
    dtype = iImage.dtype
    iImage = iImage.astype("float")
    
    if dtype.kind in ('u','i'):
        # izracunamo min in max za podatkovni tip
        iMin = np.iinfo(dtype).min
        iMax = np.iinfo(dtype).max
        iRange = iMax-iMin
    else:
        iMax = np.max(iImage)
        iMin = np.min(iImage)
        iRange = iMax - iMin
    # izvedi gamma preslikavo
    iImage = (iImage - iMin)  /float(iRange)   #skaliranje
    oImage = iImage**iGamma    # potenciranje
    oImage = float(iRange) * oImage + iMin # skaliramo nazaj v range
    
    # zaokrozevanje vrednosti
    if dtype.kind in ('u', 'i'):
        iMin = np.iinfo(dtype).min
        oImage[oImage < iMin] = iMin
        iMax = np.iinfo(dtype).max
        oImage[oImage > iMax] = iMax
        
    return oImage.astype(dtype)
