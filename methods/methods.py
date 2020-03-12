from PIL import Image
import numpy as np
import requests
from io import BytesIO
import random 
import math

def equalRGBValues(pixel):
    lightValue = sum(value for value in pixel)
    return [int(lightValue/3) for i in range(3)]

def lightPercentage(pixel):
    return sum(value for value in pixel) / (255 * 3)

def lowPassLight(pixel,lightInput):
    lightValue = sum(value for value in pixel)
    if lightValue < lightInput:
        return [0,0,0]
    else:
        return pixel

def highPassLight(pixel,lightInput):
    lightValue = sum(value for value in pixel)
    if lightValue > lightInput:
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

def getHue(pixel):
    return [value / sum(value for value in pixel) * 100 for value in pixel]

def setHue(pixel,hue):
    rawPixel = [int((lightPercentage(pixel) * .01) * (255 * 3) * value) for value in hue]
    return [color if color < 255 else 255 for color in rawPixel]

def modifyHue(pixel,details):
    totalLight = sum(value for value in pixel)
    newHue = getHue(details.newColor)
    evalHue = getHue(details.evalColor)
    evalThreshold = details.evalThreshold
    difference = pixelDistance(getHue(pixel),evalHue)
    if difference < evalThreshold:
        return setHue(pixel,newHue)
    else:
        return pixel

def shiftRed(pixel,details = None):
    if details == None:
        newPixel = sorted(pixel, reverse=True)
        return newPixel
    totalLight = sum(value for value in pixel)
    evalHue = getHue(details.evalColor)
    evalThreshold = details.evalThreshold
    difference = pixelDistance(getHue(pixel),evalHue)
    if difference < evalThreshold:
        newPixel = sorted(pixel, reverse=True)
        return newPixel
    else:
        return pixel

def shiftBlue(pixel,details = None):
    if details == None:
        newPixel = sorted(pixel)
        return newPixel
    totalLight = sum(value for value in pixel)
    evalHue = getHue(details.evalColor)
    evalThreshold = details.evalThreshold
    difference = pixelDistance(getHue(pixel),evalHue)
    if difference < evalThreshold:
        newPixel = sorted(pixel)
        return newPixel
    else:
        return pixel
               





def pixelDistance(pixelA,pixelB):
    return math.sqrt(sum((valueA - valueB)**2 for valueA,valueB in zip(pixelA,pixelB)))

def changeReds(pixel):
    lightRed = [245,192,169]
    colorDifference = pixelDistance(pixel,lightRed)
    if colorDifference < 100:
        return [value for value in pixel[::-1]]
    else:
        return pixel

def invert(pixel):
    return [abs(value - 255) for value in pixel]

def blackAndWhiteImage(pixel,empty):
    return equalRGBValues(pixel)

def resizeImage(picture,resizePercentage):
    return picture.resize(int((resizePercentage / 100) * value) for value in picture.size)

def generateNewImage(imageArray,pixelAugmentationFunction, settings = None):
    if type(imageArray) == Image.Image:
        imageArray = np.array(imageArray)
    if settings != None:
        return generateNewImageComplex(imageArray,pixelAugmentationFunction,settings)
    else:
        return generateNewImageSimple(imageArray,pixelAugmentationFunction)

def generateNewImageSimple(imageArray,pixelAugmentationFunction):
    newImageArray = [[pixelAugmentationFunction(pixel) for pixel in row] for row in imageArray]
    return Image.fromarray(np.uint8(newImageArray))

def generateNewImageComplex(imageArray,pixelAugmentationFunction,settings):
    newImageArray = [[pixelAugmentationFunction(pixel,settings) for pixel in row] for row in imageArray]
    return Image.fromarray(np.uint8(newImageArray))

def convertImageToLightValueArray(image):
    array = np.array(image)
    return np.array([[sum(value for value in pixel) for pixel in row] for row in array]).flatten()

def brighten(pixel):
    return [value + 10 if value + 10 < 255 else 253 for value in pixel]

def getImageFromUrl(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def createPixel():
    return [120,100,50]

def generateColorBlock(height,width,pixel):
    array = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(pixel)
        array.append(row)
    return Image.fromarray(np.uint8(array))

    newImageArray = [[createPixel() for pixel in range(width)] for width in range(height)]
    return newImageArray
    # print()
    # return Image.fromarray(np.uint8(newImageArray))

def generateGif(imagesArray,outputName):
    imagesArray[0].save(f"{outputName}.gif", save_all=True, loop=0, duration=100, append_images=[image for image in imagesArray[1:]])