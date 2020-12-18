sez = [1,2,3,4,5,6] # seznam števil

#rekurzivna vsota
def vsota(s):
    if s == []:
        return 0

    return s[0] + vsota(s[1:])

print(vsota(sez))