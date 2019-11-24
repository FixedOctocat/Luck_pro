def coordinatessender():
    cofflat, cofflon = 100, 200
    squares = []
    for counterlon in range(11114,11180):
        line = []
        for counterlat in range(3737,3783):
            line.append([[counterlon / cofflon,counterlat / cofflat],[(counterlon + 1) / cofflon, (counterlat + 1) / cofflat]])
        squares.append(line)
    return squares