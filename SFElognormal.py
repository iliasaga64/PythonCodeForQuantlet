import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as pl
 
# Parameter settings
print("Please input Mean mu and Variance var. Numbers should be separated with spaces. Default is 0 and 1")
para = [float(x) for x in input().split()]    
#para = [0, 1]

while len(para) != 2:
    if len(para) == 0:
        para = [0, 1]
        break
    print("Not enough or too many input arguments. Please input 2 values")
    para = [float(x) for x in input().split()]

mu  = para[0]      
var = abs(para[1]) 

# Main computation
normaxis    = np.linspace(-5 * var + mu, max(5 * var + mu, math.exp(mu) * 2 + 15 * var), 1001)
lognormaxis = np.linspace(0.0001, max(5 * var + mu, math.exp(mu) * 2 + 15 * var), 1001)
n           = norm.pdf(normaxis, mu, var)
ln          = norm.pdf(np.log(lognormaxis), mu, var)   

# Plot
pl.plot(normaxis, n, color = "blue", linewidth = 3)
pl.plot(lognormaxis, ln, color = "red", linewidth = 3, linestyle = "--")