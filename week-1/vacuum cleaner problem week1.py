rooms = {}

for room in ['A', 'B', 'C', 'D']:
    status = input("Enter status of Room " + room + " (0 = Clean, 1 = Dirty): ")
    while status not in ['0', '1']:
        status = input("Invalid input. Enter 0 or 1: ")
    rooms[room] = int(status)

location = input("Enter starting location (A/B/C/D): ").upper()
while location not in rooms:
    location = input("Invalid location. Enter A/B/C/D: ").upper()

order = ['A', 'B', 'C', 'D']
start = order.index(location)
order = order[start:] + order[:start]

print("\nInitial Room Status:", rooms)

for room in order:
    location = room
    print("\nVacuum is in Room", location)

    if rooms[location] == 1:
        print("Room", location, "is Dirty")
        rooms[location] = 0
        print("Suck action: Room", location, "Cleaned")
    else:
        print("Room", location, "is already Clean")

print("\nFinal Room Status:", rooms)

if all(status == 0 for status in rooms.values()):
    print("Goal Reached: All rooms are clean!")
