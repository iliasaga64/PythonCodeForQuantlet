import numpy as np
import seaborn as sns
from scipy.stats import binom, norm
import matplotlib.pyplot as pl
import matplotlib.patches as mpatches

# Parameter settings
print("Please input Probability p and Number n. Numbers should be separated with spaces. Default is 0.5 and 35")
para = [float(x) for x in input().split()]    
#para = [0.5, 35]
while len(para) != 2:
    if len(para) == 0:
        para = [0.5, 35]
        break
    print("Not enough or too many input arguments. Please input 2 values")
    para = [float(x) for x in input().split()]
    
p = para[0]
n = int(para[1])

# Random generation of the binomial distribution with parameters 1000*n and 0.5
bsample = binom.rvs(1, p, size = (n, 1000), random_state = 2)  

# Compute kernel density estimate & plot
x    = np.linspace(-4, 4, 1000)
pl.plot(x, norm.pdf(x, 0, 1), color="red")
samp = (np.mean(bsample, axis = 0) - p) / np.sqrt(p * (1 - p) / n)
sns.kdeplot(samp, color="green")
pl.xlabel("1000 Random Samples") 
pl.ylabel("Estimated and Normal Density")
pl.title("Asymptotic Distribution, n = " + str(n))
rp   = mpatches.Patch(color = 'red', label = 'Normal')
gp   = mpatches.Patch(color = 'green', label = 'Binomial')
pl.legend(handles = [gp, rp])