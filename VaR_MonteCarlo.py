#IMPORT NECESSARY LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


"""
Monte Carlo (GBM) Implicit Formula:
dSt = mu*St*dt + sigma*St*dW

Monte Carlo (GBM) Explicit Formula:
St = S0*exp((mu - sigma**2 / 2)*dt - sigma*Wt)

Value at Risk (Monte Carlo):
VaR = (1-c)th Percetile Of Rt

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
c = Confidence Level
zc = Standard Normal Value Corresponding To Confidence Level
Rp = Total Return Of A Path
Rt = Return On Every Step Of A Path

"""


#PARAMETERS
mu = _ #Replace the underscore with Mean Return / Expected Return (Drift)
sigma = _ #Replace the underscore with Volatility (Constant)
S0 = _ #Replace the underscore with the Initial Price
T = _ #Replace the underscore with the Number Of Years
n = _ #Replace the underscore with the Number Of Time Periods
c = _ #Replace the underscore with the Confidence Level
Ns = _ #Replace the underscore with the Number Of Simulations
zc = norm.ppf(c)
steps = T*n
dt = T/n
paths = []
Rs = []


#MULTIPLE PRICE PATHS SIMULATION PROCESS
for path in range(Ns):
  St = [S0]
  for step in range(steps):
    Z = np.random.normal(0, 1)
    exponent = (mu - sigma**2 / 2) * dt + sigma * np.sqrt(dt) * Z
    St.append(float(St[-1] * np.exp(exponent)))
  paths.append(St)


#PATHWISE SIMULATED RETURNS CALCULATION (PERIODIC)
for path in paths:
  Rp = []
  for i in range(1, len(path)):
    Rp.append((path[i] - path[i-1]) / path[i-1])
  Rs.append(Rp)


#PATHWISE SIMULATED RETURNS CALCULATION (TOTAL)
Rt = []
for path in paths:
    R = (path[-1] - path[0]) / path[0]
    Rt.append(R)


#VaR CALCULATION
VaR = S0 * (-np.percentile(Rt, (1-c)*100))
print(VaR)
print(f"Value at Risk ({c*100:.0f}% confidence, Time = {T}Y): ${VaR:.2f}")


#PLOT (SIMULATED PRICES)
for path in paths:
  plt.plot(path)
plt.xlabel("Years $(t)$")
plt.ylabel("Stock Price $(S_t)$")
plt.title("Monte Carlo Simulation")
plt.show()


#PLOT (VaR)
x = np.linspace(start = mu - 4*sigma, stop = mu + 4*sigma, num = 1000)
y = norm(loc = mu, scale = sigma).pdf(x)
plt.plot(x, y, color = "gray")
plt.fill_between(x, y, color = "cyan", alpha = 0.2)
plt.fill_between(x, y, where=(x <= -zc*sigma), color = "red", alpha=0.5)
plt.xlabel(f"Mean = {mu}\n Standard Deviation = {sigma}")
plt.ylabel("Frequency")
plt.title("Standard Normal Distribution (Returns)")
plt.axvline(-zc*sigma, linestyle = "dashed", color = "red", label = "Value at Risk")
plt.legend()
plt.show()
