class VacuumDFS:
    def __init__(self, initial_location, initial_a, initial_b):
        self.initial_state = (initial_location, initial_a, initial_b)

    def is_goal(self, state):
        _, status_a, status_b = state
        return not status_a and not status_b

    def get_successors(self, state):
        location, status_a, status_b = state
        successors = []

        if location == 'A':
            successors.append(('Suck', ('A', False, status_b)))
            successors.append(('Right', ('B', status_a, status_b)))
        else:
            successors.append(('Suck', ('B', status_a, False)))
            successors.append(('Left', ('A', status_a, status_b)))

        return successors

    def search(self):
        frontier = [(self.initial_state, [])]
        explored = set()

        while frontier:
            current_state, path = frontier.pop()

            if self.is_goal(current_state):
                return path

            if current_state not in explored:
                explored.add(current_state)
                for action, next_state in self.get_successors(current_state):
                    if next_state not in explored:
                        frontier.append((next_state, path + [action]))

        return None

problem = VacuumDFS(initial_location='A', initial_a=True, initial_b=True)
path = problem.search()

print(f"Initial State: ('A', True, True)")
print("Goal State Reached!\n")
print("Action Sequence:")
for i, action in enumerate(path, 1):
    print(f"{i}. {action}")

print(f"\nTotal Cost (Steps): {len(path)}")
