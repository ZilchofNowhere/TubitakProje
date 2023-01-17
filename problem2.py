import ParticleSwarm as ps

a: float = 6
b: float = 7
c: float = 10

def problem2(X):
    global a, b, c
    m = X[0]
    u = X[1]

    xd = (c * b) / (m * c + b - m * a)
    yd = m * xd

    xg = u * a / (m * b + a)
    yg = u * b / (m * b + a)

    xf = u / (m**2 + 1)
    yf = m * xf

    s = abs(c * b) / 2
    s1 = abs(xf * yg - xg * yf) / 2
    s2 = abs(u * yf) / 2
    s3 = abs((a * yg + xg * yf + xf * yd + xd * b) - (xg * b + xf * yg + xd * yf + a * yd)) / 2
    s4 = abs((xd * yf + c * yd) - (xf * yd + u * yf)) / 2

    q = s / 4
    return abs(s1 - q) + abs(s2 - q) + abs(s3 - q) + abs(s4 - q)
