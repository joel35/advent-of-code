FILE = "input.txt"

with open(FILE, "r") as f:
    out = [l.strip() for l in f.readlines()]

lst = []
tot = 0
for i in out:
    if not i:
        lst.append(tot)
        tot = 0
        continue
    
    tot += int(i)

lst.append(tot)

# PART 1
print(f"PART 1: {max(lst)}")

# PART 2
total_cals = sum(sorted(lst, reverse=True)[0:3])
print(f"PART 2: {total_cals}")