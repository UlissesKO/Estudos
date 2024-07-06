def in_circle(x, origin = [0,0]):
    if len(x) != 2:
        return "x is not two-dimensional!"
    elif distance(x, origin) < 1:
        return True
    else:
        return False

print(in_circle((1,1)))
False