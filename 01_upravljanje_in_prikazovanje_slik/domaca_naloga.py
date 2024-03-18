import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def loadImage(iPath):
    oImage = Image.open(iPath)
    return oImage