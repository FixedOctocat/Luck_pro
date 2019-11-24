import vk_api
with open('C:/Users/user/Desktop/access_token.txt', 'r') as file:
    access_token = file.readline().strip()
session = vk_api.VkApi(login='89168069175', token=access_token, scope=262144+4096)
session.auth()
vk = session.get_api()


def get_text_from_post(request, latitude=55.750095, longitude=37.620429, count=30):
    m = vk.newsfeed.search(count=count, q=request, latitude=latitude, longitude=longitude)
    texts = [m['items'][i]['text'] for i in range(30)]
    return texts


print(get_text_from_post('мое настроение'))










