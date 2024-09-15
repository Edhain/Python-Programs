import time
# def hour(int):
#     if (hour < 12):
#         print ('Good Morning')
#     if (hour >= 12 and hour <17 ):
#         print('Good Afternoon')
#     if (hour >=17):
#         print('Good Evening')
# t= int(time.strftime('%H'))
# # print(f"hello and {t.hour}")
# print(hour(t))
# import datetime
# hour = datetime.datetime.now().hour
# greeting = "Good morning" if 5<=hour<12 else "Good afternoon" if hour<18 else "Good evening"
# print(f"hello and {greeting}")
hour= int(time.strftime('%H'))
if (hour < 12):
    greeting = 'good morning'
if (hour >= 12 and hour <17 ):
    greeting = 'good afternoon'
if (hour >=17):
    greeting = 'good evening'
print(f"hello and {greeting}")