from math import *
import math

print(tan(3*pi/2))
# tan(theta) = dy/dx
# atan2(dy,dx) = theta (radian, pi/n의 형식)
radian1 = atan2(55, 185) # theta가 60도인 직각삼각형. 밑변1, 높이 루트3
radian2 = atan2( sqrt(3), -1) # theta가 120도인 삼각형. 밑변1, 높이 루트3
radian3 = atan2( -sqrt(3), -1) # theta가 240도, 반바퀴 + 60도
radian4 = atan2( -sqrt(3), 1) # theta가 300도, -60도
print(radian1)
print(degrees(radian1))
print(degrees(radian2))
print(degrees(radian3))
print(degrees(radian4))
print(degrees(acos(1/2)))
