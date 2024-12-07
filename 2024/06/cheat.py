from pathlib import Path

FILE = "input.txt"
FILE = "sample.txt"

path = Path(__file__).with_name(FILE)

G = {i+j*1j: c for i,r in enumerate(open(path))
               for j,c in enumerate(r.strip())}

print(G)
exit()
start = min(p for p in G if G[p] == '^')

def walk(G):
    pos, dir, seen = start, -1, set()
    while pos in G and (pos,dir) not in seen:
        seen |= {(pos,dir)}
        if G.get(pos+dir) == "#":
            dir *= -1j
        else: pos += dir
    return {p for p,_ in seen}, (pos,dir) in seen

path = walk(G)[0]
print(len(path),
      sum(walk(G | {o: '#'})[1] for o in path))