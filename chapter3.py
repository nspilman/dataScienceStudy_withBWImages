from matplotlib import pyplot as plt
from methods.methods import *
from collections import defaultdict

imageUrl = "https://images.unsplash.com/photo-1580245109369-7a1b8589e719?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjF9&auto=format&fit=crop&w=668&q=80"
imageTwoUrl = "https://images.unsplash.com/photo-1582450910569-5208d3a9b5a9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=80"
darkImage = "https://images.unsplash.com/photo-1582343104600-6d1fe40281fc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=666&q=80"
lightImage = "https://images.unsplash.com/photo-1582201957417-24546f2e643d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1652&q=80"

imageToAnalyze = getImageFromUrl(darkImage)
imageToAnalyze.show()
imageToAnalyze = resizeImage(imageToAnalyze,40)

def getLightValues(image):
    lightValueArray = convertImageToLightValueArray(image)
    lightValueCounts = defaultdict(int)
    for value in sorted(lightValueArray):
        lightValueCounts[value] += 1

    xinputs = [int(value[0]/(255*3)*100)  for value in lightValueCounts.items()] 
    yinputs = [value[1] for value in lightValueCounts.items()] 
    return xinputs, yinputs

class Metadata():
    def __init__(self,title,ylabel,xlabel):
        self.title=title,
        self.ylabel = ylabel
        if xlabel != None:
            self.xlabel = xlabel

def lineGraph(xInput,yInput,metadata):
    plt.plot(xInput,yInput,color='green',marker="o",linestyle="solid")
    plt.title(metadata.title)

    plt.ylabel(metadata.ylabel)
    return plt

def barChart(xInput,yInput,metadata):
    plt.bar(range(len(xInput)),yInput)
    plt.title(metadata.title)
    plt.ylabel(metadata.ylabel)
    plt.axis([-5,105,0,max(yInput)+30])
    plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
    return plt

def histogram(data, n_bins, cumulative=False, x_label = "", y_label = "", title = ""):
    _, ax = plt.subplots()
    ax.hist(data, n_bins = n_bins, cumulative = cumulative, color = '#539caf')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.show()

lightValueMetadata = Metadata('Pixel Count by Light Value',"Number of Pixels","Light Value")

barChart(*getLightValues(imageToAnalyze),lightValueMetadata).show()
# histogram(getLightValues(imageToAnalyze),10,False,"Light Value","Number of Pixels","Pixel Count by Light Value")
