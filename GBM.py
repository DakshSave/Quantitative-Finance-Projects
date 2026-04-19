#IMPORT NECESSARY LIBRARIES
import numpy as np
import matplotlib.pyplot as plt


"""
Geometric Brownian Motion Formula (Implicit):
dSt = mu*St*dt + sigma*St*dW

Geometric Brownian Motion Solution (Explicit):
St = S0*exp((mu - sigma**2 / 2)*dt - sigma*Wt)

Parameters:
St = Asset Price At Time t
S0 = Asset Price At Time t=0 (Initial Price)
mu = Mean Return / Expected Return (Drift)
sigma = Volatility (Constant)
dt = Time Periods
n = Number Of Time Periods
T = Number Of Years
Wt = Standard Brownian Motion (Wiener Process)
Ns = Number Of Simulations

"""


#PARAMETERS
S0 = 100
mu = 0.2
sigma = 0.2
n = 252
T = 1
Ns = 1000
dt = T / n
Rs = []


#MULTIPLE PRICE PATHS SIMULATION PROCESS
paths = []
for sim in range(Ns):
    St = [S0]
    for step in range(n):
        Z = np.random.normal(0, 1)
        exponent = (mu - sigma**2 / 2) * dt + sigma * np.sqrt(dt) * Z
        St.append(St[-1] * np.exp(exponent))
    paths.append(St)


#PATHWISE SIMULATED RETURNS CALCULATION (PERIODIC)
for path in paths:
  Rp = []
  for i in range(1, len(path)):
    Rp.append((path[i] - path[i-1]) / path[i-1])
  Rs.append(Rp)


#TIME INTERVAL TO YEARS
time = []
for i in range(n + 1):
    time.append(i * dt)


#PLOT (SIMULATED PRICES)
for path in paths:
    plt.plot(time, path)
plt.xlabel("Years $(t)$")
plt.ylabel("Stock Price $(S_t)$")
plt.title("GBM Simulation")
plt.show()


#PLOT (SIMULATED RETURNS)
for R in Rs:
   plt.plot(R)
plt.show()
