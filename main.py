import vk_api
from vk_api.exceptions import ApiError
# создайте файл config в текущей директории и укажите токен сообщества
# получить access token можно здесь: https://vkhost.github.io/
from config import TOKEN

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

# список ID пользователей, которым будут отправлены заявки
user_ids = []

for user_id in user_ids:
    try:
        responce = vk.friends.add(user_id=user_id)
        if responce == 1:
            print(f"Заявка отправлена пользователю: {user_id}")
        elif responce == 2:
            print(f"Заявка уже была отправлена пользователю: {user_id}")
        elif responce == 4:
            print(f"Вы уже друзья с: {user_id}")
        else:
            print(f"Неизвестный статус для {user_id}: {responce}")
    except ApiError as e:
        print(f"Ошибка при добавлении {user_id}: {e}")
