import math
from scipy.stats import norm

# Parameter settings
print("Please input Spot date t0, Capital V, Floor F and Expiry date T. Numbers should be separated with spaces. Default is 0, 100000, 95000 and 2")
para = [float(x) for x in input().split()]    
#para = [0, 1e+05, 95000, 2]

while len(para) != 4:
    if len(para) == 0:
        para = [0, 100000, 95000, 2]
        break
    print("Not enough or too many input arguments. Please input 4 values")
    para = [float(x) for x in input().split()]

t0 = para[0]
V  = para[1]
F  = para[2]
T  = para[3]

print("Please input Spot stock price s0, Interest r, Volatility sig, and Dividend D. Default is 100, 0.1, 0.3 and 0.02")
para2 = [float(x) for x in input().split()]    
#para2 = [100, 0.1, 0.3, 0.02]

while len(para2) != 4:
    if len(para2) == 0:
        para2 = [100, 0.1, 0.3, 0.02]
        break
    print("Not enough or too many input arguments. Please input 4 values")
    para2 = [float(x) for x in input().split()]

s0  = para2[0]
r   = para2[1]
sig = para2[2]
d   = para2[3]
tau = T - t0    # maturity tau = T - to
b   = r - d     # costs of carry

# Main computation: Newton's method
k = 0.001   # initial exercise price
t = 100.0   # initial difference between two ks

while t >= 1e-05:
    # acceptable value for difference
    y       = (math.log(s0 / k) + (b - 1 / 2 * (sig**2)) * tau) / (sig * math.sqrt(tau))         # y for BS 
    yk      = -1 / (sig * math.sqrt(tau) * k)                                                    # FOC of y respect to k
    cdfnyk1 = -math.exp(-1 * y**2 / 2) * (yk / math.sqrt(2 * math.pi))                           # FOC of PI(-y) respect to k
    cdfnyk2 = -math.exp(-1 * (y + sig * math.sqrt(tau))**2 / 2) * (yk / math.sqrt(2 * math.pi))  # FOC of PI(-y-sig*sqrt(tau))    
    pk      = math.exp(-r * tau) * k * norm.cdf(-1 * y) - math.exp((b - r) * tau) * s0 * norm.cdf(-1 * y - sig * math.sqrt(tau))  
                                                                                                 # BS put option price 
    pkk     = math.exp(-r * tau) * norm.cdf(-1 * y) + math.exp(-1 * r * tau) * k * cdfnyk1 - math.exp((b - r) * tau) * s0 * cdfnyk2         
                                                                                                 # FOC of put price respect to k
    fk      = math.exp(-d * tau) * s0 + pk - V / F * k                                           # equation 2-23 see page 30
    fkk     = pkk - V / F                                                                        # FOC of equation respect to k
    k0      = k                                                                                  # old k
    k       = k - fk / fkk                                                                       # new k
    t       = k - k0                                                                             # difference 

print("The exercise price applying NEWTON method = " + str("%.4f" % k))

print("The BS put option price = " + str("%.4f" % pk))