import time
hours=int(input("enter hours:"))
minutes=int(input("enter minutes:"))
seconds=int(input("enter seconds:"))
#converting hours and minutes into seconds
total_seconds=hours*3600+minutes*60+seconds
while total_seconds>0:
    hours,remainder=divmod(total_seconds,3600)#split hours
    minutes,seconds=divmod(remainder,60)#split minutes and seconds
    timer=f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    print(timer,end="\r")
    time.sleep(1)
    total_seconds-=1
print("time up!")
