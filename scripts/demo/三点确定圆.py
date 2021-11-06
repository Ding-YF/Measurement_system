# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# def getCircle(p1, p2, p3):
#     x21 = p2.x - p1.x
#     y21 = p2.y - p1.y
#     x32 = p3.x - p2.x
#     y32 = p3.y - p2.y
#     # three colinear
#     if (x21 * y32 - x32 * y21 == 0):
#         return None
#     xy21 = p2.x * p2.x - p1.x * p1.x + p2.y * p2.y - p1.y * p1.y
#     xy32 = p3.x * p3.x - p2.x * p2.x + p3.y * p3.y - p2.y * p2.y
#     y0 = (x32 * xy21 - x21 * xy32) / 2 * (y21 * x32 - y32 * x21)
#     x0 = (xy21 - 2 * y0 * y21) / (2.0 * x21)
#     R = ((p1.x - x0) ** 2 + (p1.y - y0) ** 2) ** 0.5
#     return x0, y0, R
#
# p1, p2, p3 = Point(0, 0), Point(4, 0), Point(2, 2)
# print(getCircle(p1, p2, p3))

def getCircle(p1, p2, p3):
    x21 = p2[0] - p1[0]
    y21 = p2[1] - p1[1]
    x32 = p3[0] - p2[0]
    y32 = p3[1] - p2[1]
    # three colinear
    if (x21 * y32 - x32 * y21 == 0):
        return None
    xy21 = p2[0] * p2[0] - p1[0] * p1[0] + p2[1] * p2[1] - p1[1] * p1[1]
    xy32 = p3[0] * p3[0] - p2[0] * p2[0] + p3[1] * p3[1] - p2[1] * p2[1]
    y0 = (x32 * xy21 - x21 * xy32) / 2 * (y21 * x32 - y32 * x21)
    x0 = (xy21 - 2 * y0 * y21) / (2.0 * x21)
    R = ((p1[0] - x0) ** 2 + (p1[1] - y0) ** 2) ** 0.5
    return x0, y0, R

# p1, p2, p3 = (0, 0), (4, 0), (2, 2)
# p1, p2, p3 = (-1.991, -0.1882), (-0.4363,-1.952), (1.541,-1.275)
# p1, p2, p3 = [274, 183],[134, 184],[212, 196]
p1, p2, p3 = [274*0.14, 183*0.15],[134*0.14, 184*0.15],[212*0.14, 196*0.15]
print(getCircle(p1, p2, p3))