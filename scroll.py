from PIL import Image
#from numpy import asarray
import sys

filename = sys.argv[1]
im = Image.open(filename)

#arr = asarray(im)

framelist = []
frameheight = 64
Nrows = im.size[1]
Ncols = im.size[0]

Nframes = Nrows - frameheight + 1

for n in range(Nframes):
	box = (0,n,Ncols,n+frameheight)
	thisframe = im.crop(box)
	framelist.append(thisframe)

framelist[0].save(filename+"_scroll.gif",save_all=True,append_images=framelist[1:])
