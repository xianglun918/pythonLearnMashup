#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats
n = 20
p = 0.3
k = np.arange(0,41)
print k
print "*"*20
binomial = stats.binom.pmf(k,n,p)
print binomial
plt.plot(k, binomial, 'o-')
plt.title('binomial:n=%i,p=%.2f (www.jb51.net)'%(n,p),fontsize=15)
plt.xlabel('number of success（脚本之家测试）',fontproperties='SimHei')
plt.ylabel('probalility of success', fontsize=15)
plt.grid(True)
plt.show()