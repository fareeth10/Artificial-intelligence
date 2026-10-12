import heapq
class PuzzleAStar:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.goal_pos = {val: (r, c) for r, row in enumerate(goal_state) for c, val in enumerate(row)}
    def manhattan_distance(self, state):
        distance = 0
        for r in range(3):
            for c in range(3):
                val = state[r][c]
                if val != 0:
                    goal_r, goal_c = self.goal_pos[val]
                    distance += abs(r - goal_r) + abs(c - goal_c)
        return distance
    def get_successors(self, state):
        successors = []
        for r in range(3):
            for c in range(3):
                if state[r][c] == 0:
                    blank_r, blank_c = r, c
                    break
        moves = [('Up', -1, 0), ('Down', 1, 0), ('Left', 0, -1), ('Right', 0, 1)]
        
        for move, dr, dc in moves:
            nr, nc = blank_r + dr, blank_c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = [list(row) for row in state]
                new_state[blank_r][blank_c], new_state[nr][nc] = new_state[nr][nc], new_state[blank_r][blank_c]
                successors.append((move, tuple(tuple(row) for row in new_state)))
        return successors
    def search(self):
        initial_h = self.manhattan_distance(self.initial_state)
        pq = [(initial_h, 0, self.initial_state, [])]
        explored = set()
        while pq:
            f, g, current_state, path = heapq.heappop(pq)
            if current_state == self.goal_state:
                return path, g
            if current_state in explored:
                continue
            explored.add(current_state)
            for move, next_state in self.get_successors(current_state):
                if next_state not in explored:
                    g_new = g + 1
                    h_new = self.manhattan_distance(next_state)
                    f_new = g_new + h_new
                    heapq.heappush(pq, (f_new, g_new, next_state, path + [move]))
        return None, -1
initial_board = (
    (1, 2, 3),
    (4, 0, 5),
    (7, 8, 6)
)
goal_board = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)
puzzle = PuzzleAStar(initial_board, goal_board)
optimal_moves, total_cost = puzzle.search()
print("Initial Board State:")
for row in initial_board:
    print(row)
print("\nGoal State Reached!\n")
print("Optimal Action Sequence:")
for i, move in enumerate(optimal_moves, 1):
    print(f"{i}. Slide {move}")
print(f"\nTotal Cost (Steps): {total_cost}")
