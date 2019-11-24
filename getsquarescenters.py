def square_centers():
    cofflat, cofflon = 50, 100
    line = []
    for counterlon in range(5557,5590):
        for counterlat in range(1868,1891):
            line.append([[counterlon / cofflon,counterlat / cofflat],[(counterlon + 1) / cofflon, (counterlat + 1) / cofflat]])
    return line