a: float = 3
b: float = 0
c: float = 3


def problem6(X):
    m = X[0]
    xf = X[1]
    xg = X[2]
    global a, b, c

    xd= -m+sqrt((m**2+4(m*xf+a**2)))/2
    yd= m*xd/2
    ye= xg/m

    xh=((m**2)*xf+xg)/((m**2)+1)
    yh=(m(xg-xf))/(m**2+1)

    s1=abs((xf*(m*(xg-xf)/(m**2 + 1))) + (m**2 * xf + xg)/(m**2 + 1)*(xg/m))/2
    s2=abs((xg* (m(xg-xf))/(m**2+1)) - (xf * (m(xg-xf)/(m**2+1))))/2
    s3a=abs((((-m+sqrt(m**2+(4*(m*xf+a**2))))/2)* (m*(xg-xf)) / (m**2+1) + (m*a*(-m+sqrt(m**2 + 4 * (m*xf + a**2)))/2 - xf)) - 
    )


    return abs(s1 - q) + abs(s2 - q) + abs(s3 - q) + abs(s4 - q)