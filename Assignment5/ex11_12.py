
def is_inside(x, y):
    if y[0] <= x[0] <= y[0] + y[2]:
        if y[1] <= x[1] <= y[1]+y[3]:
            return True
        else:
            return False
    else:
        return True
    
print (is_inside([200, 120], [140, 60, 100, 200]))

            


