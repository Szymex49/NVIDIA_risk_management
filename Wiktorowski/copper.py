import pyexpat
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import kstest, gaussian_kde, norm, t
from datetime import datetime, timedelta
from matplotlib import dates
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import datetime

# MIEDŹ
copper = pd.read_csv('copper.csv', sep = ',', encoding = 'latin-1')

## # Ceny akcji miedzi
# plt.plot(copper['Date'].values[::-1], copper['Open'].values[::-1])
# plt.show()

s = np.array(copper['Open'].values[1:])
s2 = np.array(copper['Open'].values[:-1])
r = np.log(s/s2)
plt.hist(r, bins = 30, density = True)
plt.show()

# WOLFRAM
tungstum = pd.read_csv('tungstum.csv', sep = ',')

## # Ceny akcji miedzi
# plt.plot(tungstum['Date'].values[::-1], tungstum['Open'].values[::-1])
# plt.show()

ss = np.array([float(i[1:]) for i in tungstum['Open'].values[1:]])
ss2 = np.array([float(i[1:]) for i in tungstum['Open'].values[:-1]])

p = np.log(ss/ss2)
plt.hist(p, bins = 30, density = True)
plt.show()