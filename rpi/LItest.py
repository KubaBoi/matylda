
p1 = 10 # start angle
p2 = 50 # final angle 
p = p1 # actual angle

def lerp(v0, v1, t):
  return round((1 - t) * v0 + t * v1)


i = 0
while p != p2:
    p = lerp(p1, p2, i)
    i += 0.1
    print(f"{i} {p}")