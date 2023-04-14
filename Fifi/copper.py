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

# Histogram logarytmicznych przyrostów
s = np.array(copper['Open'].values[1:])
s2 = np.array(copper['Open'].values[:-1])
r = np.log(s/s2)
plt.hist(r, bins = 30, density = True)
# plt.show()

# Kwantyle
print(np.arange(0, 1, 0.01))
# def draw_quantile():
#     alpha = np.arange()

##################################################################
