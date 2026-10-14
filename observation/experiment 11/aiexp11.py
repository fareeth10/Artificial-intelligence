class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def backtracking_search(self, assignment=None):
        if assignment is None:
            assignment = {}

        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        var = unassigned[0]

        for color in self.domains[var]:
            if self.is_consistent(var, color, assignment):
                assignment[var] = color
                
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                
                del assignment[var]

        return None

    def is_consistent(self, var, color, assignment):
        for neighbor in self.constraints[var]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

domains = {v: ['Red', 'Green', 'Blue'] for v in variables}

constraints = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

csp = MapColoringCSP(variables, domains, constraints)
solution = csp.backtracking_search()

for region, color in solution.items():
    print(f"{region} ---> {color}")
