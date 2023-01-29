import cellular as cl
import numpy as np
import os

def main():
    updaterules = cl.UpdateRules({"000":[0.1,0.9], "001":[0.03,0.97], "010":[0.6,0.4], "011":[0,1], "100":[1,0], "101":[0.5,0.5], "110":[0.75,0.25], "111":[0.3,0.7]},deterministic=False)
    mycell = cl.Cellular(64,64*8,[0,1],updaterules,initialstate="random")
    colormap = cl.Colormap({0:"255 0 0", 1:"0 255 255"})
    mycell.iterate()  
    filename = "img290123"
    mycell.savetofile(filename,colormap)
    os.system("ffmpeg -i " + filename + ".ppm " + filename + ".gif")
    os.system("python3 scroll.py " + filename + ".gif")
        
if __name__=="__main__":
    main()
