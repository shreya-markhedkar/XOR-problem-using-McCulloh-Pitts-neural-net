import numpy as np
#weights w
w11=2 #int(input('Enter weight w11: '))
w12=-1 #int(input('Enter weight w12: '))
w21=-1 #int(input('Enter weight w21: '))
w22=2 #int(input('Enter weight w22: '))
#weights v
v1=2 #int(input('Enter weight v1: '))
v2=2 #int(input('Enter weight v2: '))
#threshhold value theta
theta=2 #int(input('Enter Threshhold value theta: '))
x1=np.array([0,0,1,1])
x2=np.array([0,1,0,1])
z=np.array([0,1,1,0])
y1=np.array([0,0,0,0])
y2=np.array([0,0,0,0])
y=np.array([0,0,0,0])
c=1
while c!=0:
    zin1=x1*w11+x2*w21
    zin2=x1*w21+x2*w22
    for i in range(0,4):
        if zin1[i]>=theta:
            y1[i]=1
        else:
            y1[i]=0
        if zin2[i]>=theta:
            y2[i]=1
        else:
            y2[i]=0
        yin=y1*v1+y2*v2
        if yin[i]>=theta:
            y[i]=1  
        else:
            y[i]=0
    print('output:',y)
    if np.array_equal(y,z):
        c=0
        print('The XOR result matches the solution calculated!')
        print("McCulloch-Pitts Net for XOR function verified")
    else:
        print('Not learning. Please enter values again')
        w11=int(input('Enter weight w11: '))
        w12=int(input('Enter weight w12: '))
        w21=int(input('Enter weight w21: '))
        w22=int(input('Enter weight w22: '))
        #weights v
        v1=int(input('Enter weight v1: '))
        v2=int(input('Enter weight v2: '))
        #threshhold value theta
        theta=int(input('Enter Threshhold value theta: '))
   