def findAngle(h,m):#defining a function with arguments hours(h) and minutes(m)
    h = h % 12
    hour_hand = (h * 360) /12 +(m*360) /(12*60)#calculating hour hand
    min_hand = (m *360) /(60)#calculating min hand
    angle=abs(hour_hand - min_hand)#calculating difference between hour hand and minute hand
    if angle>180:
        angle=360-angle
    return angle
hours=int(input("hours: "))#take hours input from the user
minutes=int(input("minutes: "))#take minute input from the user
print(findAngle(hours,minutes))#print the angle between hour hand and minute hand


