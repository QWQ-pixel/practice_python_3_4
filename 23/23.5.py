def same_by(characteristic, objects):
    if objects:
        eq = characteristic(objects[0])
        return True if all(characteristic(x) == eq for x in objects) else False
    else:
        return False


values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
