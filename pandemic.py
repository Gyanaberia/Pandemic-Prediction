import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import linregress as lr
import math
covid=pd.read_csv("https://api.covid19india.org/csv/latest/case_time_series.csv")#get csv file
st=covid[covid['Date']=='14 April '].index[0]
death=np.array(covid['Total Deceased'])
t=np.arange(1,len(death)-st)
H=death[st+1:]/death[st:-1]
slope, intercept, r_value, p_value, std_err=lr(t,H)
plt.scatter(t,H,marker='.',label='H(t)')
plt.plot(t,intercept+slope*t,'r',label='fitted line')
plt.grid()
plt.xlabel('t(no of days)')
plt.ylabel('H(t)')
plt.title('Covid-19 Death ratio in India')
plt.legend()
plt.savefig('covid.png')
print(math.ceil((1-intercept)/slope))
