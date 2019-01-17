import math
import numpy as np
from scipy.stats import uniform, norm
import matplotlib.pyplot as pl

print("Please input Number of time steps n, Time step dt, Constant c and Time moment s. Numbers should be separated with spaces. Default is 20000, 0.01, 2 and 150")
para = [float(x) for x in input().split()]    
#para = [20000, 0.01, 2, 150]

while len(para) != 4:
    if len(para) == 0:
        para = [20000, 0.01, 2, 150]
        break
    print("Not enough or too many input arguments. Please input 4 values")
    para = [float(x) for x in input().split()]

n  = round(para[0])
dt = abs(para[1])
if dt == 0:
    raise ValueError("dt cannot be zero!")
c  = para[2]
s  = abs(para[3])

# Main calculation
t  = np.linspace(0, n * dt, n+1)
z 	= uniform.rvs(size = n, random_state = 1)
z 	= 2 * (z > 0.5) - 1           # scale to -1 or 1
z 	= z * c * math.sqrt(dt)       # to get finite and non-zero variance
x 	= np.append([0], np.cumsum(z))

# Computing the normal distribution
max1   = max(x)
min1   = min(x)
sigma  = math.sqrt(max(t) - s) * c
s1     = round(s / dt)
mu     = x[s1]
ndata  = np.linspace(x[s1] - 3 * sigma, x[s1] + 3 * sigma, 10000)
f      = 1 / np.sqrt(2 * math.pi * sigma**2) * np.exp(-(ndata - mu)**2 / (2 * sigma**2))
mul    = n * dt / 12 / max(f)
f      = f * mul + n * dt
y      = norm.pdf(x, mu, sigma)

# Plot
pl.plot(x, color="blue", linewidth=0.5)
pl.plot([s1, s1],[x[s1] - 3 * sigma, x[s1] + 3 * sigma], color = "black", linewidth = 0.5)
pl.plot([n, n],[x[s1] - 3 * sigma, x[s1] + 3 * sigma], color = "black", linewidth = 0.5)
pl.plot(f / dt, ndata, color="red", linewidth=1)
pl.plot([s1, n],[x[s1], x[s1]], color = "black", linewidth = 0.5, linestyle = "--")
pl.xlabel("Iteration number") 
pl.ylabel("Value")
pl.title("Wiener Process")
# Drawing the red area
a   = mu - sigma
b   = mu + sigma
ran = np.linspace(a, b, 200)
for i in ran:
    pl.plot([n, ((1 / np.sqrt(2 * math.pi * sigma**2) * np.exp(-(i - mu)**2 / (2 * sigma**2)) * mul) + n * dt) / dt], [i, i], color="red", linewidth = 2)