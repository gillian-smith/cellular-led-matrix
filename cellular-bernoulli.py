import numpy as np
#from PIL import Image

Nrows = 256
Ncols = 64
arr = np.zeros([Nrows,Ncols],dtype="i1")

for j in range(Ncols):
	r = np.random.rand()
	if r > 0.5:
		arr[0,j] = 1

# Probability of next state being 1 given the current state
update_rule_probs = {"000":0.05,
					 "001":0.2,
					 "010":0.5,
					 "011":0.7,
					 "100":0.2,
					 "101":0.6,
					 "110":0.7,
					 "111":0.95}

for i in range(Nrows-1):
	#print(arr[i,:])
	for j in range(1,Ncols-1):
		curr = ""
		for e in list(arr[i,j-1:j+2]):
			curr += str(e)
		#curr = "".join(str(e) for e in list(arr[i,j-1:j+2]))
		p = update_rule_probs[curr]
		r = np.random.rand()
		if r < p: # change next state to a 1
			arr[i+1,j] = 1
		# else: next state is already a 0

f = open("img.pbm", "w")
f.write("")

f = open("img.pbm", "a")
f.write("P1\n")
f.write(str(Ncols)+" "+str(Nrows)+"\n")

for row in range(Nrows):
	for col in range(Ncols):
		f.write(str(arr[row,col])+" ")
	f.write("\n")

#im = Image.fromarray(arr,mode="1")
#im.save("img.gif")
