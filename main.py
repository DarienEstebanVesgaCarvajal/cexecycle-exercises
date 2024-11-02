totalTime = 0

while True:
    sectionDuration = int(input("What's the duration of the section?: "))
    
    if sectionDuration == 0:
        break   

    totalTime += sectionDuration

hours = totalTime // 60
minutes = totalTime % 60

print(f"Total travel time: {hours}:{minutes:02d} hours")