total_race_time = float(input("Enter total race time (in seconds): "))
num_pit_stops = int(input("Enter number of pit stops: "))
avg_pit_duration = float(
    input("Enter average pit stop duration (in seconds): "))

total_pit_time = num_pit_stops * avg_pit_duration

pit_percentage = (total_pit_time / total_race_time) * 100
pit_percentage = round(pit_percentage, 2)

print(f"Total pit stop time: {total_pit_time} seconds")
print(f"Percentage of race in pits: {pit_percentage}%")

if pit_percentage > 5:
    print("New pit crew is required.")
