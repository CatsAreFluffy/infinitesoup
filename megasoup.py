#generate megasoup section
import random
from sys import argv
def box(x0=-32,y0=-32,dx=64,dy=64,fill=50,liveout=False):
    def generate(x,y):
        random.seed(x+y**3-x**2+x*y) # for some reason seed=y**3-3*(y+n) behaves strangely
        return random.random()
    def rleappend(c):
        nonlocal out,rep,char
        if c==char:
            rep+=1
            return
        elif rep!=0:
            if rep==1:
                rep=""
            if liveout:
                print(end=str(rep)+char)
            else:
                out+=str(rep)+char
        rep=1
        char=c
    out="x="+str(dx)+",y="+str(dy)+",rule=Confusion0\n"
    if liveout:
        print(out)
    rep=0
    char=""
    for y in range(y0,y0+dy):
        for x in range(x0,x0+dx):
            if generate(x,y)>(fill/100):
                rleappend("A")
            else:
                rleappend("B")
        rleappend("$")
    rleappend("!")
    rleappend("")
    return out
def parse(x):
    if "." in x:
        return float(x)
    else:
        return int(x)
if len(argv)<=1:
    print("Interactive mode, input space separated values.\nArguments are topleft x, topleft y, box size x, box size y, and fill %.\nYou can use = to assign arguments, ie fill=25 gives 25% fill.")
    while 1:
        x=input(">").replace("%","").split(" ")
        y=[]
        z={}
        for i in x:
            if i=="":
                continue
            if "=" in i:
                t=i.split("=")
                z[t[0]]=parse(t[1])
            else:
                y.append(parse(i))
        print(box(*y,**z))
else:
    box(*map(parse,argv[1:]),liveout=True)
