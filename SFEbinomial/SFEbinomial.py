import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as pl

# Parameter settings
print("Please input Probability p and Number n. Numbers should be separated with spaces. Default is 0.5 and 15")
para = [float(x) for x in input().split()]    
#para = [0.5, 15]
while len(para) != 2:
    if len(para) == 0:
        para = [0.5, 15]
        break
    print("Not enough or too many input arguments. Please input 2 values")
    para = [float(x) for x in input().split()]
    
p = para[0] # probability
n = para[1] # number n
x = np.linspace(1, n, n)

# Plot
y  = binom.pmf(x.astype(int), n, p)
f1 = pl.bar(x, y, color = "blue", width = 0.3)
pl.xlabel("x") 
pl.ylabel("f(x)")
pl.title("Binomial Distribution - PMF")
pl.show(f1)
z  = binom.cdf(x, n, p)
pl.subplot(111)
f2 = pl.step(x, z, color = "red", linewidth = 3)
pl.xlabel("x") 
pl.ylabel("F(x)")
pl.title("Binomial Distribution - CDF")
pl.show(f2)

# Parameter settings
print("Please input Value x, Probability p and Number n. Numbers should be separated with spaces. Default is 5, 0.5 and 15")
para1 = [float(x) for x in input().split()]    
#para1 = [5, 0.5, 15]
while len(para1) != 3:
    if len(para1) == 0:
        para1 = [5, 0.5, 15]
        break
    print("Not enough or too many input arguments. Please input 3 values")
    para1 = [float(x) for x in input().split()]

x1 = para1[0] # value of x
p1 = para1[1] # probability
n1 = para1[2] # number n

print("Binomial distribution for the specified x, p, n")
print("P(X=x) = f(x) = " + str("%.4f" % binom.pmf(x1, n1, p1)))
print("P(X<=x) = F(x) = " + str("%.4f" % binom.cdf(x1, n1, p1)))
print("P(X>=x) = 1-F(x-1) = " + str("%.4f" % (1 - binom.cdf(x1 - 1, n1, p1))))
print("P(X<x) = P(X<=x) - P(X=x) = P(X<=x-1) = F(x-1) = " + str("%.4f" % binom.cdf(x1 - 1, n1, p1)))
print("P(X>x) = P(X>=x) - P(X=x) = P(X>=x+1) = 1 - F(x) = " + str("%.4f" % (1 - binom.cdf(x1, n1, p1))))