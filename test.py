import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 1000)

uc = (
    12
    - 12*np.exp(-4*t)*np.cosh(2*np.sqrt(3)*t)
    - 8*np.sqrt(3)*np.exp(-4*t)*np.sinh(2*np.sqrt(3)*t)
)

plt.plot(t, uc)

plt.title("RLC Circuit Transient Response")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor Voltage (V)")
plt.grid(True)
# this is not GPT
plt.show()