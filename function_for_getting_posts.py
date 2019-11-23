import vk_api

access_token = '37e11a35406c1e97a304843f18c35da943c564d3bb3f4c28a20600d691fe66ac899cfc15d4abb79cc7fe6'
session = vk_api.VkApi(login='89168069175', token=access_token, scope=262144+4096)
session.auth()
vk = session.get_api()


def get_text_from_post(request, latitude=55.750095, longitude=37.620429, count=30):
    m = vk.newsfeed.search(count=count, q=request, latitude=latitude, longitude=longitude)
    texts = [m['items'][i]['text'] for i in range(30)]
    return texts


print(get_text_from_post('мое настроение'))










