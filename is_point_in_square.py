def is_point_in_square(right_high_latitude, right_high_longitude, left_down_latitude, left_down_longitude, request_latitude, request_longitude):
    # right_high_latitude - широта верхней правой точки прямоугольника
    # right_high_longitude - долгота верхней правой точки
    # left_down_latitude - широта нижней левой точки
    # left_down_longitude - долгота нижней левой точки
    # request_latitude - широта проверяемой точки
    # request_longitude - долгота проверяемой точки
    # Возвращает true, если точка внутри прямоугольника, и false, если нет


    flag = True
    if request_latitude > right_high_latitude or request_latitude < left_down_latitude:
        flag = False
    if request_longitude > right_high_longitude or request_longitude < left_down_longitude:
        flag = False
    return flag


