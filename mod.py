#!/usr/bin/env python3
import os,glob
from PIL import Image

size=128,128

for infile in glob.glob(r"./images/*"):
  file=os.path.basename(infile)
  path="/opt/icons/"
  filepath=path+file
  with Image.open(infile) as im:
    new_im=im.rotate(-90).resize(size)
    new_im.convert('RGB').save(filepath+".jpeg","JPEG")
