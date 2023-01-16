import ParticleSwarm as ps

a = 6
b = 7
c = 10

def problem2(X):
    global a, b, c
    u = X[0]
    m = X[1]

    x1 = u / (m**2 + 1)
    y1 = m * x1

    x2 = a * u / (a + m * b)
    y2 = b * u / (a + m * b)

    x3 = b * c / (b - m * (a - c))
    y3 = m * x3

    s = b * c / 2
    s1 = (x1 * y3  - x3 * y1) / 2
    s2 = u * y1 / 2
    s3 = abs(c * y2 + x2 * y1 - x1 * y2 - u * y1) / 2
    s4 = abs(a * y3 + x3 * y1 + x1 * y2 + x2 * b - a * y2 - x2 * y1 - x1 * y3 - x3 * b) / 2

    q = s / 4
    return abs(s1 - q) + abs(s2 - q) + abs(s3 - q) + abs(s4 - q)

dimensions=2
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

ps.particleswarm(problem2, bounds,p,c1,c2,vmax,tol)