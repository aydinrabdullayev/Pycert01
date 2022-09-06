hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
mins = (mins+dura)
hour = hour+mins//60
mins = mins%60
hour = hour%24

print(hour,mins,sep=':')

