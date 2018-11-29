import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as pl

# Parameter settings
print("Please input Capital V, Floor F and Horizon (years) T. Numbers should be separated with spaces. Default is 100000, 95000 and 2")
para = [float(x) for x in input().split()]    
#para = [1e+05, 95000, 2]

while len(para) != 3:
    if len(para) == 0:
        para = [100000, 95000, 2]
        break
    print("Not enough or too many input arguments. Please input 3 values")
    para = [float(x) for x in input().split()]

capital = para[0]
floor   = para[1]
T       = para[2]

print("Please input Interest r, Volatility sig, and Dividend D. Numbers should be separated with spaces. Default is 0.1, 0.3 and 0.02")
para2 = [float(x) for x in input().split()]    
#para2 = [0.1, 0.3, 0.02]

while len(para2) != 3:
    if len(para2) == 0:
        para2 = [0.1, 0.3, 0.02]
        break
    print("Not enough or too many input arguments. Please input 3 values")
    para2 = [float(x) for x in input().split()]

i = para2[0]
v = para2[1]
d = para2[2]

# Main computation
b        = i - d
S        = 100
t        = 0
start    = S/2
stop     = 2 * S
numpassi = 1000
step     = (stop - start)/(numpassi - 1)

Ks  = np.linspace(start, 200, numpassi)
y   = np.transpose((np.log(S / Ks) + (b - (v**2)/2) * T) / (math.sqrt(T) * v))
P1  = math.exp(-i * T) * Ks * np.transpose(norm.cdf(-y, 0, 1))
P   = P1 - math.exp(-(i - b) * T) * S * np.transpose(norm.cdf(-y - math.sqrt(T) * v, 0, 1))
phi = math.exp(-d * T) * S + P - Ks * (capital / floor)

if min(phi) > 0 or max(phi) < 0:
    print("Extreme value configuration")

tmp  = np.transpose(np.asarray([phi, Ks]))
tmpa = np.transpose(np.asarray([phi, Ks]))     # Note: replacing this line with tmpa = tmp produces weird glithes in Python
tmp1 = tmp[1:, :]
tmp2 = tmp[1:, :]
k    = 0
l    = 0

for j in range(numpassi): 
    if tmpa[j, 0] < 0:
        tmp1[k, :] = tmpa[j, :]
        k = k + 1
    else:
        tmp2[l, :] = tmpa[j, :]
        l = l + 1

infi = tmp1[0, :]
supi = tmp2[-1, :]
ab   = np.matmul(np.linalg.inv(np.c_[[1, 1], [supi[0], infi[0]]]), [supi[1], infi[1]])
K    = ab[0]
y    = (math.log(S/K) + (b - v / 2) * T)/(math.sqrt(T * v))
P    = math.exp(-i * T) * K * norm.cdf(-y, 0, 1) - math.exp(-(i - b) * T) * S * norm.cdf(-y - math.sqrt(T * v), 0, 1)

Shares  = floor / K * math.exp(-d * T)
Puts    = Shares * math.exp(d * T)
Sg      = np.linspace(70, 140, 8)
unvPort = (capital/S) * Sg * math.exp(d * T)
verPort = Shares * Sg * math.exp(d * T)
w       = len(Sg)
verPort = verPort * (verPort > floor) + floor * (verPort <= floor)
unvPort = np.c_[Sg, unvPort]
verPort = np.c_[Sg, verPort]

# Plot
pl.plot(unvPort[:, 0], unvPort[:, 1], color = "red", linewidth = 2)
pl.plot(verPort[:, 0], verPort[:, 1], color = "blue", linewidth = 2, linestyle="--")
pl.xlabel("Stock Price") 
pl.ylabel("Portfolio Value")
pl.title("Insured (blue) vs Non-insured (red)")

# Table output
ustockp = unvPort
vstockp = verPort
uyield  = ((ustockp[:, 1] - capital) / capital) * 100
vyield  = ((vstockp[:, 1] - capital) / capital) * 100
uvrat   = (vstockp[:, 1] / ustockp[:, 1]) * 100

np.set_printoptions(formatter = {'float_kind': lambda x: "%10.2f" % x})
print("                Not insured Port.       Insured Port.      Insured Portfolio in %")
print("   Spot Price   Value       Yield     Value       Yield    of the not Insured")
print("---------------------------------------------------------------------------------")
print(" " + str(np.c_[ustockp[:, 0], ustockp[:, 1], uyield, vstockp[:, 1], vyield, uvrat]).replace('[','').replace(']',''))