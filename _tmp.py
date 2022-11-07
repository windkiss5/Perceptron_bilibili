import math
from scipy.optimize import root

def fn(r2):
    t0 = 1.6   # 板厚
    R0 = 55    #原始板料半径
    r1 = 25    #第一次拉深凸模半径
    k = 997.6  #板料硬化系数
    n = 0.172  #板料硬化指数
    As = 400   #板料屈服强度
    Ab = 620   #板料抗拉强度
    r = 0.906  #厚向平均各向异性
    rd = 10    #第二次拉深凹模圆角半径
    r2cd = r2+rd+t0
    u = 0.12   #摩擦系数
    Rt = R0    #取到极值

    Aw = t0/(4*rd)* k * (math.log(r2cd/r2)*pow((2*(1+r))/(1+2*r),0.5))**n*(1+pow(math.e,(math.pi/2*u))) #弯曲应力

    A1 = 2*u*1.1*As*Rt/r1*pow(math.e,(math.pi/2*u))  #摩擦应力

    A2 = k*(pow(2*(1+r)/(1+2*r),(n+1)/2))*((1+n)*math.log(r1/r2cd) - 2*n*math.log((r1+Rt)/(r2cd+pow(Rt**2-r1**2+r2cd**2,0.5)))-2*n/(Rt**2-r1**2)*(r1*Rt-r2cd*pow(Rt**2-r1**2+r2cd**2,0.5)-r1**2+r2cd**2))*pow(math.e,(math.pi/2*u)) #径向应力

    Ac = k*(pow((2*(1+r)/(1+2*r)),((n+1)/2))*pow(n/math.e,n))#Leu D K 抗拉极限

    return A1+A2+Aw-Ac  #求r2

r = root(fn, 0.1)
print(r.x)