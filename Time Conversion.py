# Time Conversion
## Given a time in 12-hour AM/PM format, convert it to military (24-hour) time

time = raw_input().strip()
time, AMPM = map(int,time[:-2].split(':')), time[-2:]

if time[0] == 12 and AMPM == 'AM':
    time[0] = 0
elif time[0] < 12 and AMPM == 'PM':
    time[0] += 12

print "%02d:%02d:%02d" %(time[0],time[1],time[2])
