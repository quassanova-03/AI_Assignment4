# Telangana Map Coloring using CSP

import matplotlib.pyplot as plt
from collections import Counter

districts = [
    "Adilabad","Bhadradri","Hyderabad","Jagtial","Jangaon","Jayashankar",
    "Jogulamba","Kamareddy","Karimnagar","Khammam","Komaram Bheem",
    "Mahabubabad","Mahabubnagar","Mancherial","Medak","Medchal",
    "Mulugu","Nagarkurnool","Nalgonda","Narayanpet","Nirmal",
    "Nizamabad","Peddapalli","Rajanna","Rangareddy","Sangareddy",
    "Siddipet","Suryapet","Vikarabad","Wanaparthy","WarangalRural",
    "WarangalUrban","Yadadri"
]

neighbors = {
    "Adilabad": ["Komaram Bheem","Nirmal","Mancherial"],
    "Komaram Bheem": ["Adilabad","Mancherial"],
    "Mancherial": ["Adilabad","Komaram Bheem","Peddapalli"],
    "Nirmal": ["Adilabad","Nizamabad"],
    "Nizamabad": ["Nirmal","Kamareddy"],
    "Kamareddy": ["Nizamabad","Medak"],
    "Medak": ["Kamareddy","Sangareddy","Siddipet"],
    "Sangareddy": ["Medak","Rangareddy"],
    "Rangareddy": ["Sangareddy","Hyderabad","Vikarabad"],
    "Hyderabad": ["Rangareddy","Medchal"],
    "Medchal": ["Hyderabad"],
    "Vikarabad": ["Rangareddy","Mahabubnagar"],
    "Mahabubnagar": ["Vikarabad","Narayanpet","Wanaparthy"],
    "Narayanpet": ["Mahabubnagar"],
    "Wanaparthy": ["Mahabubnagar","Nagarkurnool"],
    "Nagarkurnool": ["Wanaparthy","Nalgonda"],
    "Nalgonda": ["Nagarkurnool","Suryapet","Yadadri"],
    "Suryapet": ["Nalgonda","Khammam"],
    "Yadadri": ["Nalgonda","Jangaon"],
    "Jangaon": ["Yadadri","WarangalUrban"],
    "WarangalUrban": ["Jangaon","WarangalRural","Karimnagar"],
    "WarangalRural": ["WarangalUrban","Mulugu"],
    "Mulugu": ["WarangalRural","Jayashankar"],
    "Jayashankar": ["Mulugu","Bhadradri"],
    "Bhadradri": ["Jayashankar","Khammam"],
    "Khammam": ["Bhadradri","Suryapet"],
    "Karimnagar": ["WarangalUrban","Peddapalli","Rajanna"],
    "Peddapalli": ["Karimnagar","Mancherial"],
    "Rajanna": ["Karimnagar","Jagtial"],
    "Jagtial": ["Rajanna","Nizamabad"],
    "Mahabubabad": ["WarangalRural"],
    "Siddipet": ["Medak"],
}

colors = ["Red","Green","Blue","Yellow"]


def is_valid(region, color, assignment):
    for neighbor in neighbors.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    for region in districts:
        if region not in assignment:
            for color in colors:
                if is_valid(region, color, assignment):
                    assignment[region] = color

                    result = backtrack(assignment)
                    if result:
                        return result

                    del assignment[region]
            return None


solution = backtrack({})


print("\nTelangana Map Coloring (One Solution)")
print("--------------------------------------")
print("{:<15} | {:<6}".format("District", "Color"))
print("--------------------------------------")

for d in districts:
    print("{:<15} | {:<6}".format(d, solution[d]))



print("\nConstraint Check:")
valid = True
for region in neighbors:
    for neighbor in neighbors[region]:
        if solution[region] == solution[neighbor]:
            valid = False

print("Valid Coloring:", valid)



count = Counter(solution.values())

print("\nColor Usage:")
for color, c in count.items():
    print(color, ":", c)


# Map-like layout
positions = {
    "Adilabad": (2, 6),
    "Komaram Bheem": (3, 6),
    "Nirmal": (2, 5),
    "Mancherial": (3, 5),
    "Nizamabad": (1, 5),
    "Kamareddy": (1, 4),
    "Medak": (1, 3),
    "Sangareddy": (0, 3),
    "Rangareddy": (1, 2),
    "Hyderabad": (2, 2),
    "Medchal": (2, 3),
    "Vikarabad": (0, 2),
    "Mahabubnagar": (1, 1),
    "Narayanpet": (0, 1),
    "Wanaparthy": (2, 1),
    "Nagarkurnool": (3, 1),
    "Nalgonda": (3, 2),
    "Suryapet": (4, 2),
    "Yadadri": (3, 3),
    "Jangaon": (4, 3),
    "WarangalUrban": (5, 3),
    "WarangalRural": (5, 2),
    "Mulugu": (6, 2),
    "Jayashankar": (6, 3),
    "Bhadradri": (7, 2),
    "Khammam": (6, 1),
    "Karimnagar": (4, 4),
    "Peddapalli": (4, 5),
    "Rajanna": (3, 4),
    "Jagtial": (2, 4),
    "Mahabubabad": (5, 1),
    "Siddipet": (2, 3),
    "Jogulamba": (0, 0)
}

color_map = {
    "Red": "red",
    "Green": "green",
    "Blue": "blue",
    "Yellow": "gold"
}


def draw_map(solution):
    plt.figure(figsize=(8,8))

    # edges
    for region in neighbors:
        for neighbor in neighbors[region]:
            x1, y1 = positions[region]
            x2, y2 = positions[neighbor]
            plt.plot([x1,x2],[y1,y2],'black',linewidth=0.5)

    # nodes
    for region,(x,y) in positions.items():
        plt.scatter(x,y,s=800,color=color_map[solution[region]])
        plt.text(x,y,region[:4],ha='center',va='center',
                 fontsize=8,color='white')

    plt.title("Telangana CSP Coloring (Improved Graph Layout)")
    plt.axis('off')
    plt.show()


draw_map(solution)