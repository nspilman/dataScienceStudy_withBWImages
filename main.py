from PIL import Image
import numpy as np
from methods.methods import *
from colorModificationDetails import *

igImage = "https://images.unsplash.com/photo-1582721478779-0ae163c05a60?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1942&q=80"

# pic = Image.open("images/stopRequested.jpg")
pic = getImageFromUrl(igImage)
# pic = generateColorBlock(100,100)
# pic.show()

# pic.quantize(255)
 
pic = pic.resize(int(.3 * value) for value in pic.size)
pic_array = np.array(pic)

# green = [125,164,50]
# orange = [211,154,53]

volcanoRed = [220,138,84]

modificationDetail = colorModification([84,138,220],volcanoRed,20)

# orangeToGreen = colorModification(green,orange)

playround_image = generateNewImage(pic_array,lowPassLight,20)
playround_image = generateNewImage(playround_image,modifyHue,modificationDetail)

playround_image.show()
# playround_image = generateNewImage(pic_array,lowPassLight,350)
# playround_image = generateNewImage(np.array(playround_image),modifyHue,orangeToGreen)
# playround_image.show()
# gifArray = []
# for i in range(10):
#     randomColor = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
#     colorDetails = colorModification(randomColor,orange)
#     gifArray.append(generateNewImage(pic_array,modifyHue,colorDetails))

# generateGif(gifArray,"stopRequested")