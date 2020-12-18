
sez = [1,2,3,4,5,6]

def vsota(s):
    if s == []:
        return 0

    return s[0] + s[1:]

print(vsota(sez))