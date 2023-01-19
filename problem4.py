xa: float = 0
ya: float = 2
xd: float = 4
yd: float = 2
xc: float = 6

def problem4(X):
    m = X[0]
    xe = X[1]
    yf = X[2]
    global a, b, c, d, e

    xh = (m**2 * xe + m * yf) / (m**2 + 1)
    yh = (m**2 * yf - m * xe) / (m**2 + 1)

    xj = (ya * xd - xa * xd - m * xe * (xa - xd)) / (ya - yd - m * xa + m * xd)
    yj = m * (ya * xd - xa * xd - xe * ya + xe * yd) / (ya - yd - m * xa + m * xd)

    xg = m * xa * yf / (m * ya + xa)
    yg = m * ya * yf / (m * ya + xa)

    xi = (m * xc * yf - xd * m * yf - m * yd * xc) / (xc - xd - m * yd)
    yi = (yd * xc - m * yd * yf) / (xc - xd - m * yd)

    s = abs((xc * yd + xd * ya) - (xa * yd)) / 2
    s1 = abs(xe * ((m**2 * yf - m * xe) / (m**2 + 1)) + ((m**2 * xe + m * yf) / (m**2 + 1)) * (m * ya * yf / (m * ya + xa)) - ((m * xa * yf / (m * ya + xa)) * (m**2 * yf - m * xe) / (m**2 + 1))) / 2
    s2 = abs((xc * (yd * xc - m * yd * yf) / (xc - xd - m * yd) + (m * xc * yf - xd * m * yf - m * yd * xc) / (xc - xd - m * yd) * (m**2 * yf - m * xe) / (m**2 + 1)) - (xe * (m**2 * yf - m * xe) / (m**2 + 1) + (m**2 * xe + m * yf) / (m**2 + 1) * (yd * xc - m * yd * yf) / (xc - xd - m * yd))) / 2
    s3 = abs((xj * yh + xh * yi + xi * yd + xd * yj) - (xh * yj + xi * yh + xd * yi + xj * yd)) / 2
    s4 = abs((xa * yg + xg * yh + xh * yj + xj * ya) - (xg * ya + xh * yg + xj * yh + xa * yj)) / 2

    q = s / 4
    return abs(s1 - q) + abs(s2 - q) + abs(s3 - q) + abs(s4 - q)
