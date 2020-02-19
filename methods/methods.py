from PIL import Image
import numpy as np
import requests
from io import BytesIO
import random 

def equalRGBValues(pixel):
    lightValue = sum(value for value in pixel)
    return [int(lightValue/3) for i in range(3)]

def compressColors(pixel):
    lightValue = sum(value for value in pixel)
    if lightValue < 200:
        return [0,0,0]
    elif lightValue > 275:
        return [255,255,255]
    else:
        return pixel

def randomColorSameLight(pixel):
    totalLight = sum(value for value in pixel)
    red = random.randint(0,totalLight)
    green = random.randint(0,totalLight - red)
    blue = totalLight - red - green
    return [red,green,blue]

def decimal(part, whole):
  return float(part)/float(whole)

def percent(part, whole):
  return decimal(part,whole) * 100

def setHue(pixel,hue):
    totalLight = sum(value for value in pixel)
    return [totalLight * (value / 100) for value in hue]

def hueTest(pixel):
    totalLight = sum(value for value in pixel)
    hue = [10,90,0]
    if(totalLight > 500):
        return setHue(pixel,hue)
    else:
        return pixel

def changeReds(pixel):
    lightRed = [245,192,169]
    colorDifference = sum(abs(pixelValue - lightRedValue) for pixelValue,lightRedValue in zip(pixel,lightRed))
    if colorDifference < 100:
        return [value for value in pixel[::-1]]
    else:
        return pixel

def blackAndWhiteImage(imageArray):
    blackAndWhiteArray = [[equalRGBValues(pixel) for pixel in row] for row in imageArray]
    return Image.fromarray(np.uint8(blackAndWhiteArray))

def createNewImageWithProgramaticPixelPerfectControl(imageArray,pixelAugmentationFunction):
    newImageArray = [[pixelAugmentationFunction(pixel) for pixel in row] for row in imageArray]
    return Image.fromarray(np.uint8(newImageArray))

def getImageFromUrl(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))