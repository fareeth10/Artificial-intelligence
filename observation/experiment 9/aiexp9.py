class TravelingSalesman:
    def __init__(self, cost_matrix):
        self.graph = cost_matrix
        self.num_cities = len(cost_matrix)
        self.min_cost = float('inf')
        self.best_tour = []

    def tsp_backtrack(self, current_city, count, current_cost, visited, tour):
        if count == self.num_cities:
            total_cost = current_cost + self.graph[current_city][tour[0]]
            if total_cost < self.min_cost:
                self.min_cost = total_cost
                self.best_tour = list(tour) + [tour[0]]
            return

        for next_city in range(self.num_cities):
            if not visited[next_city] and self.graph[current_city][next_city] > 0:
                if current_cost + self.graph[current_city][next_city] < self.min_cost:
                    visited[next_city] = True
                    tour.append(next_city)
                    
                    self.tsp_backtrack(next_city, count + 1, current_cost + self.graph[current_city][next_city], visited, tour)
                    
                    tour.pop()
                    visited[next_city] = False

    def solve(self, start_city=0):
        visited = [False] * self.num_cities
        visited[start_city] = True
        tour = [start_city]
        
        self.tsp_backtrack(start_city, 1, 0, visited, tour)
        return self.best_tour, self.min_cost

# Example distance matrix for 4 cities
cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp = TravelingSalesman(cost_matrix)
optimal_tour, minimum_cost = tsp.solve(start_city=0)

print("Optimal Tour:", " -> ".join(map(str, optimal_tour)))
print(f"Minimum Tour Cost: {minimum_cost}")
