from PIL import Image
from numpy import asarray

im = Image.open("img.gif")
arr = asarray(im)

framelist = []
frameheight = 64
Nrows = arr.shape[0]
Ncols = arr.shape[1]

Nframes = Nrows - frameheight + 1

for n in range(Nframes):
	thisframe_arr = arr[n:n+frameheight,:]
	thisframe_pil = Image.fromarray(thisframe_arr)
	framelist.append(thisframe_pil)

framelist[0].save("scroll.gif",save_all=True,append_images=framelist[1:])
