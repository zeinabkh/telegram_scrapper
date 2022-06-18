import numpy as np
from matplotlib import pyplot as plt


def f10(x):
    total = 1.10471*x[0]**2*x[1] + 0.04811*x[2]*x[3]*(14+x[1])
    return total

def taw_prim(x):
    return 6000/(np.sqrt(2)*x[0]*x[1])
def taw_dprim(x):
    total = (6000*(14+0.5*x[1])*np.sqrt(0.25*(x[1]**2+(x[0]+x[2])**2)))/(2*(0.707*x[0]*x[1]*(x[1]**2/12+0.25*(x[0]+x[2])**2)))
    return total

def taw(x):
    total = np.sqrt(taw_prim(x)**2+taw_dprim(x)**2+x[1]*taw_prim(x)*taw_dprim(x)/np.sqrt(0.25*(x[1]**2+(x[0]+x[2])**2)))
    return total
def sigma(x):
    return 504000/(x[2]**2*x[3])
def p(x):
    return 64746.022*(1-0.0282346*x[2])*x[2]*x[3]**3
def delta(x):
    return 2.1952/(x[2]**3*x[3])

def g1(x):
    return taw(x) - 13600
def g2(x):
    return sigma(x) - 30000
def g3(x):
    return x[0] - x[3]
def g4(x):
    return delta(x) - 0.25
def g5(x):
    return 6000-p(x)




bounds = [[-0.125, 10], [0.1, 10], [0.1, 10], [0.1,10]]

import DE

opt = DE.Optimizer(1000, 40, 10 ** 50, 1e-100, 0.5, 0.9)
context=opt.minimize(f10, 4, [g1, g2, g3, g4, g5], [], bounds)
best = [np.log10(log.best) for log in context.logs]
print(best[-1])
plt.plot(range(len(best)), best, label = 'DE')

import m_NMDE_con
opt = m_NMDE_con.Optimizer(1000, 40, 10 ** 50, 1e-100)
context1=opt.minimize(f10, 4, [g1, g2, g3, g4, g5], [], bounds)
print(context1.best)
best = [np.log10(log.best) for log in context1.logs]
print(best[-1])
plt.plot(range(len(best)), best, label = 'NMDE')
plt.legend()
plt.xlabel('iter')
plt.ylabel('log(f(x))')
plt.show()

standstill = [log.standstill for log in context.logs]
plt.plot(range(len(standstill)), standstill, label = 'DE')

standstill = [log.standstill for log in context1.logs]
plt.plot(range(len(standstill)), standstill, label = 'NMDE')

plt.legend()
plt.show()