import pandas as pd
import random as rd

speed,obj,dSterr=range(0,91),[0,1],(0,91)

data=pd.DataFrame(columns=['speed','object presence','Delta steer','target'])
ii,jj,kk,yy=[],[],[],[]
for c in range(4001):
    i=rd.choice(speed)
    if 0<=i<=30:
        j=rd.choice(obj)
        if j: k=rd.choice((30,50))
        else: k=rd.choice((5,20))
    elif 30<i<=60:
        j=rd.choice(obj)
        if j: k=rd.choice((20,40))
        else: k=rd.choice((5,15))
    elif 60<i<=100:
        j=rd.choice(obj)
        if j: k=rd.choice((10,20))
        else: k=rd.choice((2,8))
    ii.append(i)
    jj.append(j)
    kk.append(k)
    yy.append(0)

data.loc[:,'speed']=ii
data.loc[:,'object presence']=jj
data.loc[:,'Delta steer']=kk
data.loc[:,'target']=yy

for c in range(4001):
    i=rd.choice(speed)
    if 0<=i<=30:
        j=rd.choice(obj)
        if j: k=rd.choice((0,5))
        else: k=rd.choice((20,60))
    elif 30<i<=60:
        j=rd.choice(obj)
        if j: k=rd.choice((5,9))
        else: k=rd.choice((25,75))
    elif 60<i<=100:
        j=rd.choice(obj)
        if j: k=rd.choice((0,9))
        else: k=rd.choice((40,80))
    data.loc[len(data)]=[i,j,k,1]
    
data.to_csv('data.csv',index=False)
