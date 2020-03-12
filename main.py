from PIL import Image
import numpy as np
from methods.methods import *
from colorModificationDetails import *

# igImage = "https://lh3.googleusercontent.com/Vxi3jDSfRloMB-e9RFZS0oRpAAvQm5bS0O0J5uLIYjp9u9ToyThr1x8TYy4fnXzhFvEiTZr4VjDzmUM-L7se1IzVKz9DKWCB204hX5IFLthoEB4krJX5jF6ChHD5WLC-uBD0XkkKgs7D6N8PqE6UW5QwfZtaVCctGM47iDrSqqq4KuOxpk7bRwYU_YgipTfRD6B90C03x5Fiz4n_HDroqP6oK2KONDlJtb5i9rp3Qn4dC4l9WW6nVkwUgnrpZqbClk_FcRZeIQhon3X2LD50ZM3ED25gLB89OiDnzT3bFMAUtNkU6Z8q_VyZ17KA5OdMjvVVWkVR0O41rYtCs6-TRTyaE3fDoZCONeY5pIunY5jZ0oABfs3YSLSMhb_AeJYyzaT3shEp1Qda-_Z_0e7jDAhDB7ugUrIZrusguIFToMZiDEG-EHliKF7utj8idEJmJHGdTkZdGjTsGPsUBByS0VK6-CnRzDPYKA-3o1YY0dROKyw-QKpY3phQ2_v_ptpNxoUeQ4OJo5Hqy_Cv3E8vSDU91VDP8BXLuMT0sXL5x58TnN32_oed_fhpzTRlNa8aPp-gJTLVH9Ow1AYmX7qcUxzzs_GQL7hBEmjXvscSy4jec1009Brqf1buHL4eZzBTcJevhtn8WDr9_QPaTjD7ugJ-mrBsZYQERUQe0Nx82R_UvhrIDWyFTd7O=w1084-h1444-no"

pic = Image.open("images/lightsStrokes2.jpg").rotate(270)
# pic = getImageFromUrl(igImage)
# pic = generateColorBlock(100,100)
# pic.show()

# pic.quantize(255)
 
pic = pic.resize(int(.5 * value) for value in pic.size)
pic_array = np.array(pic)
# skyBlue = [140,178,216]

# green = [125,164,50]
# orange = [211,154,53]
# volcanoRed = [220,138,84]
# yellow = [255,180,48]

# whitesModification = colorModification(volcanoRed,[255,255,255],10)
# greensToReds = colorModification(volcanoRed,[196,204,128],40)

# orangeToGreen = colorModification(green,orange)

# playround_image = generateNewImage(pic_array,highPassLight,700)
pic_array = generateNewImage(pic_array,lowPassLight,160)
pic_array = generateNewImage(pic_array,highPassLight,550)
pic_array.show()

# generateNewImage(pic_array,shiftRed).show()
# generateNewImage(pic_array,shiftBlue).show()
# playround_image = generateNewImage(playround_image,shiftRed,whitesModification)

# playround_image.show()
# playround_image = generateNewImage(pic_array,lowPassLight,350)
# playround_image = generateNewImage(np.array(playround_image),modifyHue,orangeToGreen)
# playround_image.show()
# gifArray = []
# for i in range(10):
#     randomColor = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
#     colorDetails = colorModification(randomColor,orange)
#     gifArray.append(generateNewImage(pic_array,modifyHue,colorDetails))

# generateGif(gifArray,"stopRequested")