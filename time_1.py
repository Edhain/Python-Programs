import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
hour= int(input('enter hour'))
# if (int(time.strftime('%H')) < 12):
#     print('Good Morning')
# if (int(time.strftime('%H')) >= 12 ):
#     print('Good Afternoon')
# if (int(time.strftime('%H')) >=17):
#     print('Good Evening')
# if (int(time.strftime('%H')) >21):
#     print('Good Night')

if (hour < 12):
    print('Good Morning')
if (hour >= 12 and hour <17 ):
    print('Good Afternoon')
if (hour >=17 and hour<21):
    print('Good Evening')
if (hour >=21):
    print('Good Night')