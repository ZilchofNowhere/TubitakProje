xa: float = 0
ya: float = 2
xb: float = 0
yb: float = 0
xc: float = 3
yc: float = 0
xd: float = 2
yd: float = 2
yj: float = 3.2
xj: float = 1.5
xh: float = 1.2

def problem5(X):
    xe = X[0]
    xf = X[1]
    m = X[2]
    global xa, ya, xb,yb, xc,yc, xd, yd, yj, xj

    yh=(m*(xf-xe)) / (m**2 +1)
    yi=m*((xe*yd-xe*yj+yj*xd-yd*xj) / (yj-yd-m*xj+m*xd))
    xi =(m*xe*xd-m*xe*xj+yj*xd-yd*xj)/(yj-yd-m*xj+m*xd)
    xg= (xj*(xf-m*ya) / (m*yj-m*ya+xj))
    yg=((xf*yj-xf*ya-xj*ya) / (m*yj-m*ya+xj))

    sa=abs((xa*yb+xb*yc+xc*yd+xd*ya) - (xb*ya+xc*yb+xd*yc+xa*yd))/2
    sb=abs((xj*ya+xd*yj) - (xd*ya+xj*yd)) / 2
    s=sa+sb
    s1a=abs(xe*(m*(xf-xe)/(m**2+1))+ (m**2 * xe + xf) / (m**2+1)* ya) / 2
    s1b = abs((xj*(xf-m*ya))/(m*yj-m*ya+xj)*ya + ((m**2 * xe + xf)/(m**2 +1)) * (xf*yj-xf*ya-xj*ya) /(m*yj-m*ya+xj)-
    (m**2 * xe + xf)/(m**2 + 1) * ya +(xj*(xf-m*ya))/(m*yj-m*ya+xj) * (m*(xf-xe))/(m**2 + 1)) / 2
    s1 = s1a+s1b

    s2=abs((m*(xf-xe))/(m**2 + 1) * (xf-xe)) / 2

    s3a=abs(xc*yd + (xd*(m*(xf-xe) / (m**2 + 1))) - (xf* (m*(xf-xe) / (m**2 + 1))) + (m**2 * xf - xe) / (m**2 + 1) * yd) / 2
    s3b=abs((xi*yh + xh*yd + xd*yi) - (xh*yi + xd*yh + xi*yd))/2
    s3= s3a+s3b
    
    s4=abs(xj*yg + xg*yh + xh*yi + xi*yj) - (xg*yj+xh*yg+xi*yh+xj*yi) / 2


    return abs(s1-(s/4)) + abs(s2-(s/4)) + abs(s3-(s/4)) + abs(s4-(s/4))
