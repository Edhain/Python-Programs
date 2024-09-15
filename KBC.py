import time
def hour :
    hour= int(time.strftime('%H'))
    if (hour < 12):
        print('Good Morning')
    if (hour >= 12 and hour <17 ):
        print('Good Afternoon')
    if (hour >=17):
        print('Good Evening')

print(f"Hello and {hour}")