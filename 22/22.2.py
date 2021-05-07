def partial_sums(*args):
    part_sum, count = [], len(args) + 1
    for i in range(count):
        if i == 0:
            part_sum.insert(i, 0)
        else:
            part_sum.insert(i, sum(args[:i]))
    return part_sum


print(partial_sums(13))
