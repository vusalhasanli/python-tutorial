pets = { "dog": 3.5, "cat": 2.5, "bird": 1.75, "gerbil": 5.25 }

def pick_pet(pets):
    try:
        inp = input()
        print(pets[inp])
    except:
        print("Sorry, we do not have {}. Please, try again...".format(inp))
        inp = input()
        print(pets[inp])
pick_pet(pets)