
x = [255, 255]

import random
#import numpy

rr = random.random
bitstring = b''

for i in range(x[0]):
   for y in range(x[1]):
       bitstring = bitstring +\
           bytes(int(rr()*255)) + b',' +\
           bytes(int(rr()*255)) + b',' +\
           bytes(int(rr()*255)) + b',255,255,255,'

bitstring = bitstring[:-1]

from PIL import Image
im = Image.frombytes(mode='RGBA', size=x, data=bitstring)
im.show()







