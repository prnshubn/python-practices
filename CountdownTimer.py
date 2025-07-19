import time

timer_seconds=int(input("Enter timer in seconds for how long: "))

for x in range(timer_seconds, 0, -1):
    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)%24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up")