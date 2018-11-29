import math
import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as pl
 
# Parameter settings
print("Please input Number of time steps n, Time Step dt, Constant c and Number of paths k. Numbers should be separated with spaces. Default is 200, 0.5, 1 and 5")
para = [float(x) for x in input().split()]    
#para = [200, 0.5, 1, 5]

while len(para) != 4:
    if len(para) == 0:
        para = [200, 0.5, 1, 5]
        break
    print("Not enough or too many input arguments. Please input 4 values")
    para = [float(x) for x in input().split()]
n  = round(para[0])         # number of time steps
dt = para[1]                # time step
c  = para[2]                # constant
k  = round(para[3])         # number of paths

# Main computation
t 	= np.linspace(0, n * dt, n + 1)
z 	= uniform.rvs(size = (n, k))
z 	= 2 * (z > 0.5) - 1           # scale to -1 or 1
z 	= z * c * math.sqrt(dt)       # to get finite and non-zero variance
zz = np.cumsum(z, axis = 0)
x 	= np.append(np.zeros([1, k]), zz, axis=0)

# Output
for i in range(k):
    pl.plot(x[:, i], color = (uniform.rvs(random_state = i), uniform.rvs(random_state = i + 1000), uniform.rvs(random_state = i + 2000)), linewidth = 2)  
pl.xlabel("Time") 
pl.ylabel("Values of Process")
pl.title("Wiener Process")