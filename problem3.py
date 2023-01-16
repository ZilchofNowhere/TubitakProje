import ParticleSwarm as ps

a: float = 5
b: float = 7
c: float = 8
d: float = 3

def problem3(X):
    global a, b, c,d 
    u = X[0]
    v = X[1]
    m = X[2]

    x1 = (m**2 * u + v) / (m**2 + 1)
    y1 = m * (x1 - u)

    x2 = v * a / (b * m + a)
    y2 = x2 * (b / a**2)

    x3 = ((a - c) * (m * u + d) + c * (d - b)) / (m + d - b)
    y3 = m * (x3 - u)

    x4 = -m * u / (d / c - m)
    y4 = -d * m * u / (d - c * m)

    x5 = v * c / (d + c * m)
    y5 = d / c * x5

    s = (b * c - a * d) / 2
    s1 = abs(x4 * y1 + x1 * y2 - x2 * y1 - x1 * y4) / 2
    s2 = ((x1 * y4 + x4 * y5 + x5 * y1) - (x1 * y5 + x5 * y4 + x4 * y1)) / 2
    s3 = abs(x3 * y1 + x1 * y5 + x5 * d + c * y3 - x3 * d - c * y5 - x5 * y1 - x1 * y3) / 2
    s4 = abs(a * y2 + x2 * y1 + x1 * y3 + x3 * b - a * y3 - x3 * y1 - x1 * y2 - x2 * b) / 2

    q = s / 4
    return abs(s1 - q) + abs(s2 - q) + abs(s3 - q) + abs(s4 - q)


dimensions=3
dimension_bounds=[-6,6]
bounds=[0]*dimensions #creating 5 dimensional bounds
for i in range(dimensions):
    bounds[i]=dimension_bounds

#creates bounds [[x1,x2],[x3,x4],[x5,x6]....]    
    
p=60 #shouldn't really change 
vmax=(dimension_bounds[1]-dimension_bounds[0])*0.75
c1=2.8 #shouldn't really change
c2=1.3 #shouldn't really change
tol=0.00000000000001

ps.particleswarm(problem3, bounds,p,c1,c2,vmax,tol)