import toolbox.BVPSolver as BVPS
import math as m
def p(x):
    return (-2/x)

def q(x):
    return (2/(x**2))

def r(x):
    return (m.sin(m.log(x))/(x**2))

def y(x):
    return ((1.139)*x)+(-0.039/(x**2))-(0.3*m.sin(m.log(x)))-(0.1*m.cos(m.log(x)))

print("Actual y(2)=", y(2))
yp=BVPS.LinearShooting(p,q,r,1,2,1,2,0.1,10)
print("Predicted y(2)=",yp[-1])