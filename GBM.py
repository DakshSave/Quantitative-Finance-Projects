#IMPORT NECESSARY LIBRARIES
import numpy as np
import matplotlib.pyplot as plt


"""
Geometric Brownian Motion Formula (Implicit):
dSt = mu*St*dt + sigma*St*dW

Geometric Brownian Motion Solution (Explicit):
St = S0*exp((mu - sigma**2 / 2)*t - sigma*Wt)

Parameters:
St = Asset Price At Time t
S0 = Asset Price At Time t=0 (Initial Price)
mu = Mean Return / Expected Return (Drift)
sigma = Volatility (Constant)
t = Time Periods
n = Number Of Time Periods
T = Number Of Years
Wt = Standard Brownian Motion (Wiener Process)
Ns = Number Of Simulations

"""


#PARAMETERS
S0 = _ #Replace the underscore with the Initial Price.
mu = _ #Replace the underscore with the Mean Return / Expected Return (Drift).
sigma = _ #Replace the underscore with the Standard Deviation / Volatility.
n = _ #Replace the underscore with the Number Of Time Periods.
T = _ #Replace the underscore with the Number Of Years.
Ns = _ #Replace the underscore with the Number Of Simulations.
t = T / n
Rs = []


#MULTIPLE PRICE PATHS SIMULATION PROCESS
paths = []
for sim in range(Ns):
    S = [S0]
    for step in range(n):
        Z = np.random.normal(0, 1)
        exponent = (mu - sigma**2 / 2) * t + sigma * np.sqrt(t) * Z
        S.append(S[-1] * np.exp(exponent))
    paths.append(S)


#PATHWISE SIMULATED RETURNS CALCULATION (PERIODIC)
for path in paths:
  Rp = []
  for i in range(1, len(path)):
    Rp.append((path[i] - path[i-1]) / path[i-1])
  Rs.append(Rp)


#TIME INTERVAL TO YEARS
time = []
for i in range(n + 1):
    time.append(i * t)


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
