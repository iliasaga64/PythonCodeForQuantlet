import numpy as np
from scipy.stats import uniform, norm
import seaborn as sns
import matplotlib.pyplot as pl
import matplotlib.patches as mpatches

# Parameter settings
print("Please input Number of Observations n, Number of trajectories k and probability p. Numbers should be separated with spaces. Default is 100, 100 and 0.5")
para = [float(x) for x in input().split()]    
#para = [100, 100, 0.5]

while len(para) != 3:
    if len(para) == 0:
        para = [100, 100, 0.5]
        break
    print("Not enough or too many input arguments. Please input 3 values")
    para = [float(x) for x in input().split()]
    
n = round(para[0])           # number of observations
k = round(para[1])           # number of trajectories
p = para[2]                  # probability of positive step being realised   
             
if p > 1 or p < 0:
    raise ValueError("p and q must be smaller than 1 and in sum larger than 0 but smaller than 1!")

# Main computation
z     = uniform.rvs(size = (n, k), random_state = 1)  # uniform random numbers
z     = ((np.floor(-z + p)) + 0.5) * 2                # scale ordinary binomial processes
x     = np.sum(z, axis = 1)                           # end values of the k binomial processes
h     = 0.3 * (max(x) - min(x))                       # bandwidth used to estimate the density of end values
sns.kdeplot(x, bw = h, color = "blue")                # Kernel-based density estimation with specified bandwidth
trend = n * (2 * p - 1)
std   = np.sqrt(4 * n * p * (1 - p))
norm  = std * norm.rvs(size = k, random_state = 1) + trend
sns.kdeplot(norm, bw = h, color = "red", linestyle='--')
pl.xlabel("N = " + str(n) + ", Bandwidth = " + str(round(h)))
pl.ylabel("Density")
pl.title("Distribution of generated binomial processes")
rp    = mpatches.Patch(color = 'red', label = 'Normal')
bp    = mpatches.Patch(color = 'blue', label = 'Binomial')
pl.legend(handles = [bp, rp])