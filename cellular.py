import numpy as np

class Cellular:
    def __init__(self,width,length,statespace,updaterules,initialstate="zeros",dynamiclength=False):
        self.length = length
        self.width = width
        self.arr = np.zeros([length,width],dtype="i1")
        self.statespace = statespace
        self.updaterules = updaterules
        if initialstate == "random":
            self.arr[0,:] = np.random.choice(statespace,width)#,p=...)
        elif initialstate != "zeros":
            self.arr[0,:] = initialstate

    def __str__(self):
        return "cellular automaton of width " + str(self.width) + " and length " + str(self.length)
        
    def iterate(self):
        for i in range(self.length-1):
            for j in range(1,self.width-1):
                curr = ""
                for e in list(self.arr[i,j-1:j+2]):
                    curr += str(e)
                if self.updaterules.deterministic:
                    self.arr[i+1,j] = self.updaterules.ruledict[curr]
                else:
                    probs = self.updaterules.ruledict[curr]
                    self.arr[i+1,j] = np.random.choice(self.statespace,p=probs)
                    
    def savetofile(self,filename,colormap):
        f = open(filename+".ppm", "w")
        f.write("")
        f = open(filename+".ppm", "a")
        f.write("P3\n")
        f.write(str(self.width)+" "+str(self.length)+" "+str(255)+"\n")
        for row in range(self.length):
            for col in range(self.width):
                f.write(colormap.colormap[self.arr[row,col]]+" ")
                f.write("\n")
        
class Colormap:
    def __init__(self,colordict):
        self.colormap = colordict        
        
class UpdateRules:
    def __init__(self,ruledict,deterministic=True):
        self.ruledict = ruledict
        self.deterministic = deterministic
    
def main():
    updaterules = UpdateRules({"000":0, "001":1, "010":0, "011":0, "100":1, "101":0, "110":0, "111":0})
    mycell = Cellular(64,64,[0,1],updaterules,initialstate="random")
    colormap = Colormap({0:"255 0 0", 1:"0 255 255"})
    mycell.iterate()  
    mycell.savetofile("img290123",colormap)
        
if __name__=="__main__":
    main()
