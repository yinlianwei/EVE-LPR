__author__ = 'Evenvi'
import tesseract
import cv

image = cv.LoadImage("./img/plate.png",cv.CV_LOAD_IMAGE_GRAYSCALE)

def recognize(image):
    api = tesseract.TessBaseAPI()
    api.Init(".","eng",tesseract.OEM_DEFAULT)
    api.SetPageSegMode(tesseract.PSM_AUTO)

    tesseract.SetCvImage(image, api)
    text = api.GetUTF8Text()
    conf = api.MeanTextConf()

    return text

print recognize(image)