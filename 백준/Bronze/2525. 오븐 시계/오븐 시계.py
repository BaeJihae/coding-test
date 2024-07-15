hours, minutes = map(int, input().split())

required_time = int(input())

minutes += required_time

hours += ( minutes // 60 )
minutes = minutes % 60

if hours >= 24:
    hours %= 24

print(hours, minutes)