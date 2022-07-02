dust = 60
'''
if dust > 150 : 
    print('매우나쁨')
elif 80<dust<=150 :
    print('나쁨')
elif 30<dust<=80 :
    print('보통')
else :
    print('좋음')
'''

def dustconsider(x) :
    if dust > 150 : 
        print('매우나쁨')
    elif dust>80 :
        print('나쁨')
    elif dust>30 :
        print('보통')
    elif dust>=0 :
        print('좋음')
    else:
        print('error')
dustconsider(dust)