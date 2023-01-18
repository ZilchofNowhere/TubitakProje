a: float = 3
b: float = 5
c: float = 7
d: float = 4
e: float = 10

def problem4(X):
    u = X[0]
    v = X[1]
    m = X[2]
    global a, b, c, d, e

    x1 = (m**2 * u + m * v) / (m**2 + 1)
    y1 = m * (x1 - u)

    x2 = m * a * v / (b * m + a)
    y2 = (b / a) * x2

    x3 = ((c - a) * (-m * v - b) + a*d - a*b) / (d - b - m*c + m*a)
    y3 = m * (x3 - u)

    x4 = m * (v * c - e * v + e * d) / (d * m + c - e)
    y4 = d / (c-e) * (x4 - e)

    s = abs(e * d + b * c - a * d) / 2
    s1 = abs(a * y2 + x2 * y1 + x1 * y3 + x3 * b - a * y3 - x3 * y1 - x1 * y2 - x2 * b) / 2
    s2 = abs(u * y1 + x1 * y2 - x2 * y1) / 2
    s3 = abs(c * y4 + x4 * y1 - x1 * y4 - u * y1) / 2
    s4 = abs(x3 * y1 + x1 * y4 + x4 * d + c * y3 - x3 * d - c * y4 - x4 * y1 - x1 * y3) / 2

    q = s / 4
    return abs(s1 - q) + abs(s2 - q) + abs(s3 - q) + abs(s4 - q)
