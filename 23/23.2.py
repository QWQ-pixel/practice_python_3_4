def find_farthest_orbit(list_of_orbits):
    max_s = []
    for i in list_of_orbits:
        if i[0] != i[1]:
            max_s.append(i[0] * i[1])
        else:
            max_s.append(0)
    index = max_s.index(max(max_s))
    return list_of_orbits[index]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
