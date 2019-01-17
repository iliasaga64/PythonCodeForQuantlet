import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as pl

# Parameter settings
print("Please input Number of Observations n, Number of trajectories k and probability p. Numbers should be separated with spaces. Default is 100, 3 and 0.6")
para = [float(x) for x in input().split()]    
#para = [100, 3, 0.6]

while len(para) != 3:
    if len(para) == 0:
        para = [100, 3, 0.6]
        break
    print("Not enough or too many input arguments. Please input 3 values")
    para = [float(x) for x in input().split()]
n = round(para[0])         # number of observations
k = round(para[1])         # number of trajectories
p = para[2]                # probability of positive step being realised

# Main computation
t       = np.linspace(0, n, n + 1)
trend   = t * (2 * p - 1)
std     = np.sqrt(4 * t * p * (1 - p))
s_1     = trend + 2 * std  # upper confidence band
s_2     = trend - 2 * std  # lower confidence band
z       = uniform.rvs(loc = (p - 1), scale = 1, size = (k, n), random_state = 1)  # matrix of uniform random numbers
z       = (z > 0) * 1
z       = z * 2 - 1
walk    = np.zeros((k,n))

for i in range(2,n):
    walk[:, i] = walk[:, i - 1] + z[:, i]

if p == 0.5:
    bound = [-20, 20]
elif p > 0.5:
    bound = [-5, p * 70]
else:
    bound = [(p - 1) * 70, 5]
    
# Plot trajectories    
for i in range(k):
    pl.plot(walk[i, ], color = (uniform.rvs(random_state = i), uniform.rvs(random_state = i + 1000), uniform.rvs(random_state = i + 2000)), linewidth = 2.5)
pl.ylim(bound)
pl.xlabel("Time") 
pl.ylabel("Process")
pl.title(str(k) + " Binomial Processes with p = " + str(p))

pl.plot(s_1, linewidth = 0.5, color = (0.6, 0.6, 0.6))   # upper confidence interval boundary
pl.plot(s_2, linewidth = 0.5, color = (0.6, 0.6, 0.6))   # lower confidence interval boundary
pl.plot(trend, linewidth = 2.5, color = "black")         # trend line 