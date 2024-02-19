creatures = {}
while True:
    line = input()
    if line == "Where do they live?":
        for creature, homes in creatures.items():
            homes = "-".join(homes)
            print(f"{creature.capitalize()}\t{homes}")
        break
    line = line.strip().lower()
    creature, home = line.split()
    if len(set(creature).intersection(home)) >= 2:
        if creatures.get(creature):
            creatures[creature].append(home)
        else:
            creatures[creature] = [home]
