from PIL import Image
import numpy as np
from methods.methods import *

baseBlue = [10,90,244]
baseGreen = [20,230,96]
baseBlack = [255,255,255]
darkGrey = [50,50,50]
allRed = [255,0,0]
darkPixel = [1,1,1]

blueHue = [value / sum(value for value in baseBlue) * 100 for value in baseBlue]
blackHue = [int(value / sum(value for value in baseBlack) * 100) for value in baseBlack]
darkGreyHue = [int(value / sum(value for value in darkGrey) * 100) for value in darkGrey]
assert blackHue == darkGreyHue

def generateColorGif(hue,name):
    colors = []
    for lightPercentage in range(100):
        rawColor = [int((lightPercentage * .0001) * (255 * 3) * value) for value in hue]
        newColor = [color if color < 255 else 255 for color in rawColor]
        image = generateColorBlock(200,200,newColor)
        colors.append(image)
    colors[0].save(f"{name}.gif", save_all=True, append_images=[color for color in colors[1:]])

baseBlueLightPercentage = sum(value for value in baseBlue) / (255*3)
newColor =[int((baseBlueLightPercentage * .01) * (255 * 3) * value) for value in blueHue]

# print(blackHue)

generateColorGif(blueHue,'blue')
generateColorGif(blackHue,'grey')
generateColorGif(allRed,'red')

greenHue = [int(value / sum(value for value in baseGreen) * 100) for value in baseGreen]

# pic = generateColorBlock(100,100,blueHue)
# new = generateColorBlock(100,100,newColor)
# pic.show()
# new.show()

# print(sum(value for value in blueHue))
# print(sum(value for value in newBlue))

# pic.show()
# new.show()