#IMPORT NECESSARY LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


#PARAMETERS
mu = 0.14
sigma = 0.30
S0 = 100.0
T = 1
n = 252
Ns = 1000
c = 0.95
zc = norm.ppf(c)
steps = T*n
t = T/n
paths = []
Rs = []


#MULTIPLE PRICE PATHS SIMULATION PROCESS
for path in range(Ns):
  S = [S0]
  for step in range(steps):
    Z = np.random.normal(0, 1)
    exponent = (mu - sigma**2 / 2) * t + sigma * np.sqrt(t) * Z
    S.append(float(S[-1] * np.exp(exponent)))
  paths.append(S)


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
