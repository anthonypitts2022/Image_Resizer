# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:20:11 2019

@author: antho
"""

#from gimpfu import *
import os
from PIL import Image
import sys

def __main__():
    for imageFile in os.listdir("C:\\Users\\antho\\Downloads\\IEORImages"):
        if imageFile=="resized" or imageFile=="notResized":
            continue
        file, ext = os.path.splitext(imageFile)
        try:
            with Image.open("C:\\Users\\antho\\Downloads\\IEORImages\\"+ imageFile) as im:
                width, height = im.size
                if(width==height):
                    im = im.resize((300,300),Image.ANTIALIAS)
                    im.save("C:\\Users\\antho\\Downloads\\IEORImages\\resized\\" + imageFile)
                    width, height = im.size
                    im.close()
                    os.remove("C:\\Users\\antho\\Downloads\\IEORImages\\" +imageFile)
                else:
                    im.save("C:\\Users\\antho\\Downloads\\IEORImages\\notResized\\"+imageFile)
                    os.remove("C:\\Users\\antho\\Downloads\\IEORImages\\" +imageFile)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print("failed on : " + imageFile)
            continue
        
__main__()
        