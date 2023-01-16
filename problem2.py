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
