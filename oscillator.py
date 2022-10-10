import numpy as np
import matplotlib.pyplot as plt

fs = 44000 #sampling freq
f = 440 #signal freq
vlen = fs #length of vector to hold samples 
r = 1 #r parameter

w_0 = 2 * np.pi *f/fs
sinw_0 = np.sin(w_0)
cosw_0 = np.cos(w_0)

y = vlen*[0] #fill with 0s
x = np.linspace(0,1,fs) #segmented linespace for 1 second

for n in range(0,vlen): #oscillator
    if n == 0:
        y[n]=0
    if n == 1:
        y[n]=r*sinw_0+2*r*cosw_0*y[n-1]
    else:
        y[n]=2*r*cosw_0*y[n-1]-r*r*y[n-2]
    print(y[n])

plt.plot(x,np.array(y))
plt.show()
