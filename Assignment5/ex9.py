#9
def get_even_list(l):
    even_number = []
    for i in l:
        if i %2 == 0:
            even_number.append(i)
    return even_number