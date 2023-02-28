#import cellular as cl
import numpy as np
import os

from pathlib import Path
import time

from PIL import Image, ImageSequence
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def array2image(arr,colormap):
    arr_RGB = np.zeros((arr.shape[0],arr.shape[1],3),dtype='uint8')
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            color = colormap[arr[i,j]]
            arr_RGB[i,j,0] = color[0]
            arr_RGB[i,j,1] = color[2]
            arr_RGB[i,j,2] = color[1]
    return Image.fromarray(arr_RGB,'RGB')
    
def normalise(L): 
    sumL = sum(L)
    return list(map(lambda x:x/sumL, L))

def main():
    # # random red and blue
    # S = [0,1]
    # updaterules = {"000":[0,1], "001":[1,0], "010":[0,1], "011":[0.5,0.5], "100":[0.1,0.9], "101":[0.4,0.6], "110":[0.8,0.2], "111":[0.45,0.55]}
    # colormap = {0:(0, 0, 200), 1:(255, 0, 0)}
    
    # lava
    # S = [0,1,2]
    # eps = 0.1
    # updaterules = {
        # "000":normalise([3,eps,eps]),
        # "001":normalise([2,1,eps]),
        # "002":normalise([2,eps,1]),
        # "010":normalise([2,1,eps]),
        # "011":normalise([1,2,eps]),
        # "012":normalise([1,1,1]),
        # "020":normalise([2,eps,1]),
        # "021":normalise([1,1,1]),
        # "022":normalise([1,eps,2]),
        # "100":normalise([2,1,eps]),
        # "101":normalise([1,2,eps]), 
        # "102":normalise([1,1,1]),
        # "110":normalise([1,2,0]),
        # "111":normalise([eps,3,eps]),
        # "112":normalise([eps,2,1]), 
        # "120":normalise([1,1,1]),        
        # "121":normalise([eps,2,1]),
        # "122":normalise([eps,1,2]),
        # "200":normalise([2,eps,1]),
        # "201":normalise([1,1,1]),
        # "202":normalise([1,eps,2]),
        # "210":normalise([1,1,1]),
        # "211":normalise([eps,2,1]),
        # "212":normalise([eps,1,2]),
        # "220":normalise([1,eps,2]),
        # "221":normalise([eps,1,2]),
        # "222":normalise([eps,eps,3])
    # }
    # #colormap = {0:(36, 0, 0), 1:(180, 0, 0), 2:(222, 100, 0)}
    # colormap = {0:(255,255,255), 1:(180, 0, 180), 2:(100, 100, 222)}
    
    # black and white
    S = [0,1]
    updaterules = {
        "000":[0.9,0.1],
        "001":[0.7,0.3],
        "010":[0.5,0.5],
        "011":[0.3,0.7],
        "100":[0.7,0.3],
        "101":[0.5,0.5],
        "110":[0.3,0.7],
        "111":[0.9,0.1]
    }
    colormap = {0:(0,0,0),1:(255,255,255)}
    
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'
    matrix = RGBMatrix(options=options)
    
    frame_array = np.zeros((64,64),dtype="i1")
    currline = np.zeros(64,dtype="i1")
    # initial condition
    currline = np.random.choice(S,size=64)
    frame_array[-1,:] = currline
    nextline = np.zeros(64,dtype="i1")
    
    counter = 0
    while True:
        counter += 1
        for j in range(0,currline.size):
            curr = ""
            # periodic boundary conditions
            if j==0: 
                curr = str(currline[-1]) + str(currline[0]) + str(currline[1])
            elif j==currline.size-1:
                curr = str(currline[j-1]) + str(currline[j]) + str(currline[0])
            else:
                for e in list(currline[j-1:j+2]):
                    curr += str(e)
            probs = updaterules[curr]
            nextline[j] = np.random.choice(S,p=probs)
        frame_array[:-1,:] = frame_array[1:,:] # shift all rows up by one
        frame_array[-1,:] = nextline
        currline = nextline

        frame = array2image(frame_array,colormap)
        #frame = frame.convert('RGB').resize((64,64))
        matrix.SetImage(frame)
        #print(frame)
        #frame.save("frames/img" + str(int(counter)) + ".png")
        time.sleep(1/100)
        
if __name__=="__main__":
    main()
