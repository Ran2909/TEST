for big in range(1, 34):
    for medium in range(1, 51):
        for small in range(2, 199, 2):
            if 3*big + 2*medium + small/2 == 100 and big + medium + small == 100:
                print("需要大马{0}匹、中马{1}匹、小马{2}匹".format(big,medium,small))