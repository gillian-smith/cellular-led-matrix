import cellular as cl
import numpy as np
import os

def main():
	S = [0,1,2]
	updaterules = cl.UpdateRules({"000":[1,0,0],
		"001":[0.8,0.2,0],
		"002":[0.8,0,0.2],
		"010":[0.6,0.4,0],
		"011":[0.2,0.8,0],
		"012":[0.2,0.6,0.2],
		"020":[0.6,0,0.4],
		"021":[0.2,0.2,0.6],
		"022":[0.2,0,0.8],
		"100":[0.8,0.2,0], 
		"101":[0.4,0.6,0], 
		"102":[0.6,0.2,0.2],
		"110":[0.2,0.8,0],
		"111":[0,1,0],
		"112":[0,0.8,0.2], 
		"120":[0.2,0.2,0.6],		
		"121":[0,0.6,0.4],
		"122":[0,0.2,0.8],
		"200":[0.8,0,0.2],
		"201":[0.6,0.2,0.2],
		"202":[0.4,0,0.6],
		"210":[0.2,0.6,0.2],
		"211":[0,0.8,0.2],
		"212":[0,0.4,0.6],
		"220":[0.2,0,0.8],
		"221":[0,0.2,0.8],
		"222":[0,0,1]			
		},deterministic=False)
	mycell = cl.Cellular(64,64*8,S,updaterules,initialstate="random")
	colormap = cl.Colormap({0:"36 0 0", 1:"180 0 0", 2:"252 72 0"})
	mycell.iterate()  
	filename = "lava"
	mycell.savetofile(filename,colormap)
	os.system("ffmpeg -i " + filename + ".ppm " + filename + ".gif")
	os.system("python3 scroll.py " + filename + ".gif")
	
if __name__=="__main__":
	main()
