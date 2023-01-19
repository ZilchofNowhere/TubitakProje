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

    s = 2* (a**3) / 3

    s1=abs((xf*(m*(xg-xf)/(m**2 + 1))) + (m**2 * xf + xg)/(m**2 + 1)*(xg/m))/2
    s2=abs((xg* (m(xg-xf))/(m**2+1)) - (xf * (m(xg-xf)/(m**2+1))))/2
    s3a=abs((((-m+sqrt(m**2+(4*(m*xf+a**2))))/2)* (m*(xg-xf)) / (m**2+1) + (m*a*(-m+sqrt(m**2 + 4 * (m*xf + a**2)))/2 - xf)) - 
    (((m**2 * xf + xg) / (m**2+1)) * m * (-m * sqrt((m**2+ 4 * (m * xf + a**2)))/ 2 - xf)) + xg * (m*(xg-xf)/(m**2+1)))

    s3b=2*(a**3)/3 - (a**2 * (-m + sqrt(m**2 + 4 * (m*xf + a**2))) / 2 + ((-m + sqrt(m**2 + 4*(m*xf+ a**2))) / 2) / 3) - m * a
    ((-m + sqrt(m**2+4*(m*xf+a**2))) / 2 -xf) + (m * ((-m+sqrt(m**2 + 4*(m*xf+ a**2))) / 2 - xf) * ((-m+sqrt(m**2+4*(m*xf+a**2)))/2))/2

    s3=s3a+s3b

    s4a=abs((m**2 * xf + xg)/ (m**2+1) * m *( (-m + sqrt(m**2 + 4 * (m * xf + a ** 2))) / 2 - xf) + (-m + sqrt(m**2 + 4 * (xf+ a**2)))/ 2
    * a**2 - ((m**2 * xf + xg)/ (m**2+1) * (xg/m) + ((-m+sqrt(m**2+4*(xf+a**2)))/2 * (m * (xg-xf)) / (m**2+1))))
    
    s4b=(a**2 * (-m+sqrt(m**2+ 4 * (m*xf+a**2)))/2 - (((-m+(sqrt(m**2+ 4 * (m*xf+a**2)))) / 2) / 3)  ) - (((a**2+m * (-m+sqrt(m**2+ 4 *(m * xf + a**2))) / 2 - xf)) * ((-m+sqrt(m**2+4*(m*xf+a**2))) / 2)/2)

    s4=s4a+s4b

    return abs(s1-(s/18)) + abs(s2-(s/9)) + abs(s3-(s/6)) + abs(s4-(2*s/3)) 