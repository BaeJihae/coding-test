hours, minutes = map(int, input().split())

if minutes >= 45:
    minutes -= 45
else:
    minutes = 15 + minutes
    hours -= 1

if hours < 0:
    hours = 23

print(hours, minutes)