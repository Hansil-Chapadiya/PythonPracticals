def score():
    return 89

score()
with open("HA13.txt") as f :
    HA13 = int(f.read())

if HA13 < score() :
    with open ("HA13.txt",'w') as f:
        f.write(str(score()))