import vk

user_service_access_key = open("user_service_access_key.txt").read().splitlines()
service_access_key = open("service_access_key.txt").read().splitlines()
session1 = vk.Session(user_service_access_key)
session2 = vk.Session(service_access_key)
api1 = vk.API(session1, v=5.101)
api2 = vk.API(session2, v=5.101)

dict_of_areas_publics = {}

def filter_of_areas_groups(area_name):
    dict_of_areas_publics[area_name] = []
    all_found_groups = api1.groups.search(q=area_name)
    for i in range(len(all_found_groups['items'])):
        information_of_group = api2.groups.getById(group_ids=all_found_groups['items'][i]['id'],
                                                   fields="description")
        group_description = information_of_group[0]['description']
        if "новости" in group_description:
            dict_of_areas_publics[area_name].append([
                all_found_groups['items'][i]['id'],
                all_found_groups['items'][i]['name']
            ])
    return dict_of_areas_publics

def posts_to_text(area_name):
    text_all_posts = ''
    for i in dict_of_areas_publics[area_name]:
        all_group_posts = api2.wall.get(owner_id=-i[0])
        for i in range(len(all_group_posts['items'])):
            text_all_posts = text_all_posts + all_group_posts['items'][i]['text']
    return text_all_posts

def find_factor(area_name):
    max = 0
    for i in dict_of_areas_publics[area_name]:
        number_of_members = api2.groups.getMembers(group_id=i)['count']
        if number_of_members > max:
            max = number_of_members
    for i in dict_of_areas_publics[area_name]:
        number_of_members = api2.groups.getMembers(group_id=i)['count']
        i.append(number_of_members/max)
    return dict_of_areas_publics
