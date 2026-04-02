# Crypt-Arithmetic: TWO + TWO = FOUR

letters = ['T','W','O','F','U','R']
digits = list(range(10))

solutions = []
steps = 0


def is_valid(assign):

    if 'T' in assign and assign['T'] == 0:
        return False
    if 'F' in assign and assign['F'] == 0:
        return False

    if len(assign) == 6:
        t, w, o = assign['T'], assign['W'], assign['O']
        f, u, r = assign['F'], assign['U'], assign['R']

        two = t*100 + w*10 + o
        four = f*1000 + o*100 + u*10 + r

        return 2 * two == four

    return True


def backtrack(assign):
    global steps
    steps += 1

    if len(assign) == len(letters):
        solutions.append(assign.copy())
        return

    for letter in letters:
        if letter not in assign:

            for d in digits:
                if d not in assign.values():

                    assign[letter] = d

                    if is_valid(assign):
                        backtrack(assign)

                    del assign[letter]

            return


backtrack({})

print(f"\nTotal Solutions Found: {len(solutions)}")


while True:
    user_input = input(f"\nChoose solution (1-{len(solutions)}) or type 'end': ")

    if user_input.lower() == "end":
        print("Program ended.")
        break

    if not user_input.isdigit():
        print("Invalid input.")
        continue

    choice = int(user_input)

    if choice < 1 or choice > len(solutions):
        print("Out of range.")
        continue

    sol = solutions[choice - 1]

    t, w, o = sol['T'], sol['W'], sol['O']
    f, u, r = sol['F'], sol['U'], sol['R']

    two = t*100 + w*10 + o
    four = f*1000 + o*100 + u*10 + r

    print("\nSolution:")
    print(f"T={t}, W={w}, O={o}")
    print(f"F={f}, U={u}, R={r}")

    print("\n  TWO")
    print("+ TWO")
    print("------")
    print(" FOUR\n")

    print(f"  {two}")
    print(f"+ {two}")
    print("------")
    print(f" {four}")