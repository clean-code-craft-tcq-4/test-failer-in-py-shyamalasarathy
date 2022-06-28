def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    Length_Colors = len(minor_colors)
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            global index0
            pair_number = i * Length_Colors + j + 1
            if (i == 0) and (j == 0):
                index0 = pair_number
            print(f'{pair_number:<3} | {major:<7} | {minor}')
    return len(major_colors) * len(minor_colors)

result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")

#Indexing error
assert(index0==1)
