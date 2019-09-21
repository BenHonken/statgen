import random
def statgen():
    ss=[]
    while len(ss)<6:
        s1=[]
        while len(s1)<4:
            roll=random.randint(1, 6)
            s1.append(roll)
        s2=0
        while len(s1)>1:
            gone=max(s1)
            s2=s2+gone
            s1.remove(gone)
        ss.append(s2)
    return ss
reroll='y'
while reroll=='y':
    stats=statgen()
    print (stats)
    reroll=input('Would you like to reroll? y/n ')

