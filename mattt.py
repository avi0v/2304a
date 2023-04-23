import matplotlib.pyplot as plt 
import numpy as np 

a=np.arange(1,11)
b=np.random.uniform(13,15,10)

fig=plt.figure(figsize=(5,5))

#feeding value
plt.plot(a,b)

#setting limits

plt.xlim(0,12)
plt.ylim(12,15)

plt.show()