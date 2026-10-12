class VacuumWorld:
    def __init__(self, location, status_a, status_b):
        self.location = location
        self.rooms = {'A': status_a, 'B': status_b}
        self.cost = 0

    def step(self):
        if self.rooms[self.location]:
            print(f"Room {self.location} is DIRTY. Action: Suck")
            self.rooms[self.location] = False
            self.cost += 1
        else:
            next_location = 'B' if self.location == 'A' else 'A'
            print(f"Room {self.location} is clean. Action: Move to {next_location}")
            self.location = next_location
            self.cost += 1

    def is_solved(self):
        return not self.rooms['A'] and not self.rooms['B']

world = VacuumWorld(location='A', status_a=True, status_b=True)

step_count = 0
while not world.is_solved() and step_count < 10:
    print(f"--- Step {step_count + 1} (Location: {world.location}, Rooms: {world.rooms}) ---")
    world.step()
    step_count += 1

print(f"\nEnvironment cleaned in {world.cost} steps!")
