# Australia Map Coloring using CSP (Backtracking)

import matplotlib.pyplot as plt

regions = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']

solutions = []



def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def backtrack(assignment):
    if len(assignment) == len(regions):
        solutions.append(assignment.copy())
        return

    for region in regions:
        if region not in assignment:
            for color in colors:
                if is_valid(region, color, assignment):
                    assignment[region] = color
                    backtrack(assignment)
                    del assignment[region]
            return


backtrack({})



positions = {
    'WA': (0, 2),
    'NT': (1, 3),
    'SA': (1, 2),
    'Q': (2, 3),
    'NSW': (2, 2),
    'V': (2, 1),
    'T': (2, 0)
}

color_map = {
    'Red': 'red',
    'Green': 'green',
    'Blue': 'blue'
}


def draw_map(solution):
    plt.figure(figsize=(6,6))

    for region in neighbors:
        for neighbor in neighbors[region]:
            x1, y1 = positions[region]
            x2, y2 = positions[neighbor]
            plt.plot([x1, x2], [y1, y2], 'black', linewidth=1)

    for region, (x, y) in positions.items():
        plt.scatter(x, y, s=2000, color=color_map[solution[region]])
        plt.text(x, y, region, ha='center', va='center',
                 color='white', fontsize=12, weight='bold')

    plt.title("Australia Map Coloring (CSP Graph View)")
    plt.axis('off')
    plt.show()



print(f"\nTotal Solutions Found: {len(solutions)}")

while True:
    user_input = input("\nEnter solution number (1-{}) or type 'end': ".format(len(solutions)))

    if user_input.lower() == "end":
        print("Program ended.")
        break

    if not user_input.isdigit():
        print("Invalid input. Enter a number.")
        continue

    choice = int(user_input)

    if choice < 1 or choice > len(solutions):
        print("Number out of range.")
        continue

    solution = solutions[choice - 1]

    print("\nAustralia Map Coloring (Solution {})".format(choice))
    print("-------------------")
    print("{:<5} | {:<6}".format("State", "Color"))
    print("-------------------")

    for region in regions:
        print("{:<5} | {:<6}".format(region, solution[region]))

    draw_map(solution)