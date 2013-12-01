__author__ = 'Evenvi'
from SimpleCV import Image, Display, Color, DrawingLayer
import numpy as np

def cuteImg(pack_blob_zoom,pack_blob_size):
    oriImg = Image("./img/original.jpg")
    cropImg = oriImg.crop(pack_blob_zoom[0]*2,pack_blob_zoom[1]*2.05,pack_blob_size[0]*0.85,pack_blob_size[1]*0.62,centered=True)
    cropImg.save("./img/dest5.jpg")
    #cropImg.show()