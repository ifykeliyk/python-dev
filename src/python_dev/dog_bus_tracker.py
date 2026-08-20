MAX_SEATS = 10

bus = {
    1: {"name": "Cujo", "breed": "Labrador", "pickup": "7:00 AM", "dropoff": "4:00 PM"},
    2: {"name": "Kojo", "breed": "Great Dane", "pickup": "7:15 AM", "dropoff": "4:15 PM"},
    3: {"name": "Benny", "breed": "Golden Retriever", "pickup": "7:30 AM", "dropoff": "4:30 PM"},
}

print("-- Starting roster --")
for seat, info in bus.items():
    print(f"Seat {seat}: {info['name']} (pickup {info['pickup']})")

if len(bus) < MAX_SEATS:
    seat_num = len(bus) + 1
    new_pet = {
        "name": "Rex",
        "breed": "Collie",
        "pickup": "7:45 AM",
        "dropoff": "4:45 PM",
    }
    bus[seat_num] = new_pet
    print(f"\n {new_pet['name']} boards (seat {seat_num}).")
else:
    print("\n No free seats.")

print("\n roster after pickup")
for seat, info in bus.items():
    print(f"Seat {seat}: {info['name']}")


remove_name = input("\nWho goes home early? ").strip().lower()

seat_to_remove = 0
for seat, info in bus.items():
    if info['name'].lower() == remove_name:
        seat_to_remove = seat
        break

if seat_to_remove:
    gone = bus.pop(seat_to_remove)
    print(f"\n {gone['name']} (seat {seat_to_remove}) heads home early.")
else:
    print(f"\n No passenger name '{remove_name}' on the bus.")


print("\n Final roster")
for seat, info in bus.items():
    print(f"Seat {seat}: {info['name']} (drop-off {info['dropoff']})")
