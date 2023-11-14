import sys
sys.path.append('./toolbox/')

import Deg2Solver as D2S

def LinearShooting(p,q,r,alpha,beta,a,b,h,n):
    """ 
    This functions solves BVP, and returns the function value and its derivative at all the mesh
    points , using the linear shooting and RK4 method.
    PROBLEM:
    Given: ypp(t,y,yp)=p(t)*yp(t)+q(t)*y(t)+r(t) ;
           y(a)=alpha ;
           y(b)=beta ;
           a+h*n=b
    """
    def f1(X,Y,YP):
        return (p(X)*YP)+(q(X)*Y)+r(X)
    
    def f2(X,Y,YP):
        return (p(X)*YP)+(q(X)*Y)
    
    (y1is,y1pis)=D2S.Deg2RK4(f1,a,alpha,0,h,n)
    (y2is,y2pis)=D2S.Deg2RK4(f2,a,0,1,h,n)
    yps=[]
    ys=[alpha]
    for i in range(n+1):
        yps.append(y1pis[i]+(((beta-y1is[n])/y2is[n])*y2pis[i]))
    for i in range(1,n+1):
        ys.append(y1is[i]+(((beta-y1is[n])/y2is[n])*y2is[i]))
    
    return (ys,yps)
