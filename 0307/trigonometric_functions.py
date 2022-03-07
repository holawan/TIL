#제 2코싸인
def shot(my,tg,hole) :
    r = 15/2
    a = sqrt((my[0]-hole[0])**2 + (my[1]-hole[1])**2)
    b = sqrt((tg[0]-hole[0])**2 + (tg[1]-hole[1])**2)
    c = sqrt((my[0]-tg[0])**2 + (my[1]-tg[1])**2)
    C = acos((a**2 + b**2 - c**2)/(2*a*b))

    theta1 = atan2(abs(hole[1]-my[1]),abs(hole[0]-my[0]))
    if my[1] > tg[1] :

        d = sqrt((a*sin(C))**2 + (a*cos(C)+b+2*r)**2)
    else :
        d= sqrt((a*sin(C))**2 + (a*cos(C)-b-2*r)**2)


    theta2 = acos((a**2 + d**2 - (b+2*r)**2)/(2*a*d))

    if hole[1]>tg[1] :
        angle = degrees(theta1+theta2)
    else :
        angle = degrees(theta1-theta2)
    print(f'theta1: {degrees(theta1)}, theta2: {degrees(theta2)}, +: {degrees(theta1+theta2)}, -: {degrees(theta1-theta2)}')
    power = 140
    return angle, power

#코싸인 법칙
#hole~target
a = sqrt((hole[0]-tg[0])**2 + (hole[1]-tg[1])**2)
#hole_x ~ target_x
b = abs(hole[0]-tg[0])
#hole_y ~ target_y
c = abs(hole[1] - tg[1])
beta = acos(c/a)
print(a,b,c)
#가상의 공과 hole간의 거리
new_a = a + 2*r
#가상의 공과 hole_x 거리
new_b = new_a*sin(beta)
#가상의 공과 hole_y 거리
new_c = new_a*cos(beta)
print(new_a,new_b,new_c)
#가상의 공 좌표
sudo = [abs(hole[0]-new_b),abs(hole[1]-new_c)]
print(sudo)
theta = atan2(abs(sudo[1]-my[1]) , abs(sudo[0]-my[0]))
print(sudo[1]-my[1],sudo[0]-my[0])
print(degrees((theta)))