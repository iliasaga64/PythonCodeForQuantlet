import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as pl

# Parameter settings
print("Please input Number of Observations n, Number of trajectories k and probabilities p and q. Numbers should be separated with spaces. Default is 100, 3, 0.25 and 0.25")
para = [float(x) for x in input().split()]    
#para = [100, 3, 0.25, 0.25]

while len(para) != 4:
    if len(para) == 0:
        para = [100, 3, 0.25, 0.25]
        break
    print("Not enough or too many input arguments. Please input 4 values")
    para = [float(x) for x in input().split()]
        
n = round(para[0])         # number of observations
k = round(para[1])         # number of trajectories
p = para[2]                # probability of positive step being realised
q = para[3]                # probability of negative step being realised

if p + q > 1 or p + q < 0:
    raise ValueError("p and q must be smaller than 1 and in sum larger than 0 but smaller than 1!")
    
# Main simulation
u     = 1  # n of t increments Z_1,...,Z_t take value u
d     = 1  # m of t increments Z_1,...,Z_t take value d
t     = np.linspace(1, n, n)
trend = t * (p * u - q * d)
std   = np.sqrt(t * (p * (1 - p) + q * (1 - q) + 2 * p * q * u * d))
s1    = trend + 2 * std                              # upper confidence band
s2    = trend - 2 * std                              # lower confidence band
z     = uniform.rvs(size = (k,n), random_state = 1)  # uniform random numbers
z     = (-1) * (z < q) + (z > (1 - p))
x     = np.cumsum(z, axis = 1)

# Plot trajectories    
for i in range(k):
    pl.plot(x[i, :], color = (uniform.rvs(random_state = i), uniform.rvs(random_state = i + 1000), uniform.rvs(random_state = i + 2000)), linewidth = 2.5)  # all other trajectories
pl.xlabel("Time") 
pl.ylabel("Process")
pl.title(str(k) + " Trinomial Processes with p = " + str(p) + " and q = " + str(q))
    
pl.plot(s1, linewidth = 0.5, color = (0.6, 0.6, 0.6))       # upper confidence interval boundary
pl.plot(s2, linewidth = 0.5, color = (0.6, 0.6, 0.6))       # lower confidence interval boundary
pl.plot(trend, linewidth = 2.5, color = "black")            # trend line