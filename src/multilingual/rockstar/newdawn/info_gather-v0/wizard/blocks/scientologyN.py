import pickle
from lolita import fury
import re
from getFromPickle import returnAList
#from simpleStorage import storeAList
#from shakeThatBootyR import neuron
from newTestN import toyProject
# pause it a little bit.
uselessPrick=[0,1]
# what is this fuck?
# write those splitable items into it.
coreLoop=returnAList()
coreCount=len(coreLoop)
jokeBook=[]
for k in range(coreCount+1):
    jokeBook.append([])
# what is idle all about?
simpleFunc=(lambda x: x.split(':',1))

def simpleDerive(x):
    shitOut=simpleFunc(x)
    print("--you are dead--")
    print(shitOut)
    print("--you are dead--")
    stopFuck=[re.findall(r'\w+',shitOut[0])[0]]
    try:
        stopFuck.append(re.findall(r'[^ ].+$',shitOut[1])[0])
    except:
        return (stopFuck+[''])
    # now we have a list which length is 1, so we can tell this apart from len 2.
    return stopFuck

"""papi=""
with open("scavenger.pickle","rb") as _file:
    papi=pickle.load(_file)
    print (papi)
#fuck
papi0=""
with open("scavenger0.pickle","rb") as _file:
    papi0=pickle.load(_file)
    print (papi0)
"""
pap=""
greatWall=(lambda x: x[:-1] if x[-1]=="\n" else x)
#greatWall0=(lambda x: x[:-1] if x[-1]==" " else x)
#greatWall1=(lambda x: x[1:] if x[1]==" " else x)
greatWall2=(lambda x: "".join([p for p in x if p !=" "]))
with open("scavenger1.pickle","rb") as _file:
    pap=pickle.load(_file)
#    print (pap)

joker=(lambda nope0:nope0[:-1] if nope0[-1]=="\n" else nope0)
joke=(lambda nope0: list(filter((lambda x:x!=""),nope0)))
greatWall3=(lambda x:list(map((lambda y:greatWall2(y)),joker(x.split(",")))))
gfw=(lambda x:list(map((lambda y:chr(int(y[2:],16)) if len(y)>1  and y[:2]=="U+" else y ),greatWall3(x))))
nope=""
with open("core.log","r") as tits:
    nope=tits.read()

with open(joker(nope)+"blocks.txt","r") as dickhead:
    shit=dickhead.read().split("\n")
    shit0=joker(joke(shit))
#    print(shit0)
    fuckme=[]
    for m in range(len(pap)):
        fuckme.append([])
    for r,k in enumerate(shit0):
        for r0,k0 in enumerate(pap):
            for r1,k1 in enumerate(k0):
                redis=fury(k1,k)
                if redis==True:
                    fuckme[r0].append([r,r1])
                else:
                    pass
    print("GIBBRISH")
    print(fuckme)
    print("GIBBRISH")
    milk=(lambda fuckme0,a,b: [r[0] for r in fuckme0[a] if r[0] in [r0[0] for r0 in fuckme0[b]]] )
#    print(fuckme)
    dizzy=milk(fuckme,0,1)
    print("--spliter a--")
    print(dizzy)
    print("--spliter b--")
    for kids in range(len(dizzy)):
        #first round.
#        jokeBook=[]
        discJokey=[list(range(coreCount)),[]]
#        for j in range(coreCount):
#            discJokey.append(False)
#        discJokey=list(enumerate(discJokey))
        royal=dizzy[kids]
        print("--spliter c--")
        royalty=shit0[royal][1:-1]
        print(royalty)
        jokeBook[coreCount].append(royalty)
#        try:
#            toyProject(2,[royalty])
#            print("TITLE INTEGRATED")
#        except:
#            print("DUPLICATE CODE 2")
        # fucking savangers.
        # this is the main title.
        print("--spliter d--")
        if kids<(len(dizzy)-1):
            royal0=dizzy[kids+1]
        else:
            royal0=len(shit0)
        royal+=1
        for jokes in range(royal0-royal):
            try:
                wolf=shit0[jokes+royal]
                if ':' in wolf:
                    print("--spliter e--")
                    # you shall build a checklist.
                    shakeItOff=greatWall(wolf)
                    # to create a function which is usable.
                    director=simpleDerive(shakeItOff)
#                    jokeBook.append(director[0])
                    print(shakeItOff)
                    print("--spliter FBI--")
                    print(director)
                    cookYourFood=coreLoop.index(director[0])
                    discJokey[1].append(cookYourFood)
                    #jokeBook[cookYourFood].append(gfw(director[1]) if cookYourFood in uselessPrick else director[1])
                    if cookYourFood not in [0,1,3]:
                        jokeBook[cookYourFood].append(director[1])
                    elif cookYourFood == 3:
                        jokeBook[cookYourFood].append(list(map((lambda x:str(int('0x'+x,0))), director[1].split(':'))))
                    else:
                        jokeBook[cookYourFood].append(list(map((lambda x: greatWall2(x)), director[1].split(','))) if len(director[1]) > 1 else [])
                    print("--spliter f--")
                else:
                    pass
            except:
                pass
        for i0 in [p for p in discJokey[0] if p not in discJokey[1]]:
            if i0 not in [0,1,3]:
                jokeBook[i0].append('')
            else:
                jokeBook[i0].append([])
#        print("--asshole is here--")
#        print(jokeBook)
#        coreLoop+=jokeBook
#        print("--asshole is here--")
print("--finalblow--")
# do that thing.
'''
for svn, jokeBookN in enumerate(jokeBook):
    print(svn,len(jokeBookN),jokeBookN)'''
for jb in range(len(jokeBook[2])):
    # this is the type.
    a0,b0,c0,d0,e0=jokeBook[0][jb],jokeBook[1][jb],jokeBook[2][jb],jokeBook[3][jb],jokeBook[4][jb]
    if c0!='':
        toyProject(0,[c0,e0])
    else:
        pass
    toyProject(2,[d0[0],d0[1],e0])
    if a0!=[]:
        for a1 in a0:
            toyProject(3,[a1,e0])
    else:
        pass
    if b0!=[]:
        for b1 in b0:
            toyProject(1,[b1,e0])
    else:
        pass
#coreLoop=list(set(coreLoop))
#for indexOf,coreInIt in enumerate(jokeBook):
#    print(indexOf,len(coreInIt),coreInIt.count([]),coreInIt)
'''
for i1 in range(len(jokeBook[0])):
    kv2,kv3=jokeBook[6][i1],jokeBook[0][i1]
    if kv3!=[]:
        for kv0 in kv3:
            try:
                toyProject(0,[kv0,kv2])
                print("--remember me--")
            except:
                print("--fuckup 0--")
    kentuckyFried=[]
    for i0 in [2,4]:
        kv4=jokeBook[i0][i1]
        if kv4!=[]:
            kentuckyFried+=kv4
    for kv1 in list(set(kentuckyFried)):
        try:
            print(kv1[0])
            print(ord(kv1[0]))
            toyProject(1,[ord(kv1[0]),kv2])
            print("--remember your char--")
            if len(kv1)>1:
                for r0 in range(len(kv1)-1):
                    try:
                        print(kv1[1+r0])
                        print(ord(kv1[1+r0]))
                        toyProject(2,[ord(kv1[r0]),ord(kv1[1+r0]),kv2])
                        print("--break your fucking neck bitch--")
                    except:
                        print("--fuckup 2--")
            else:
                pass
        except:
            print("--fuckup 1--")
            '''
#storeAList(coreLoop)
print("--finalblow--")
#    print(shit0[-1],len(shit0)-1)
    # do other shit.
#    print(shit0)
# notice that this is a superior leveler.
# it evolves slower. sure. it takes more time. hard to break.
# yes you can make things into matricies but it is with loss.
# the method is zoom in and zoom out.
# self similarity. one word can be one article, and one article can also be one word.
