import vk_api
with open('password', 'r') as file:
    password = file.readline().strip()
session = vk_api.VkApi(login='89168069175', password=password, scope=262144+4096)
session.auth(token_only=True)
vk = session.get_api()


def get_text_from_post(request, latitude=55.750095, longitude=37.620429, count=30):
    m = vk.newsfeed.search(count=count, q=request, latitude=latitude, longitude=longitude)
    texts = [m['items'][i]['text'] for i in range(30)]
    return m


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


def posts_get(m):
    h = m[0]
    l = m[1]
    right_high_latitude, right_high_longitude = h
    left_down_latitude, left_down_longitude = l
    posts_near = get_text_from_post('мое настроение', latitude=(right_high_latitude-left_down_latitude)/2, longitude=(right_high_longitude-left_down_longitude)/2, count=100)
    posts = []
    for i in range(30):
        lat = posts_near['items'][i]['geo']['place']['latitude']
        lon = posts_near['items'][i]['geo']['place']['longitude']
        f = is_point_in_square(right_high_latitude, right_high_longitude, left_down_latitude, left_down_longitude, lat, lon)
        if f:
            posts.append(posts_near['items'][i]['text'])
    return posts
