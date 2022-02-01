import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

keyboard = VkKeyboard(inline=False)
keyboard.add_button('Капкейки', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Торты', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Пряники', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_openlink_button('Больше выбора ', link='https://vk.com/alisco_astrakhan')

#капкейки
keyboard1 = VkKeyboard(inline=False)
keyboard1.add_button('Классика', color=VkKeyboardColor.PRIMARY)
keyboard1.add_line()
keyboard1.add_button('Капкейки + ягоды, фрукты', color=VkKeyboardColor.PRIMARY)
keyboard1.add_line()
keyboard1.add_button('Капкейки + пряники', color=VkKeyboardColor.PRIMARY)
keyboard1.add_line()
keyboard1.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

#торты
keyboard2 = VkKeyboard(inline=False)
keyboard2.add_button('Торт сердце/цифра/буква/фигура', color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button('Карамельный', color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

#пряники
keyboard3 = VkKeyboard(inline=False)
keyboard3.add_button('Пряники стандарт', color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button('Пряничные букеты', color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

def write_message(sender, message, keyboard):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                       'keyboard': keyboard.get_keyboard()})
def send_photo(sender, message, keyboard):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),'attachment':','.join(attachments),
                                       'keyboard': keyboard.get_keyboard()})


token = 'key'
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
upload = VkUpload(authorize)

image7 = 'C:/Users/name/PycharmProjects/helloworld/bot_vk/bouquet.jpg'
image = 'сlassic.jpg'
image2 ='cupcake.jpg'
image3 ='cup.jpg'
image4 ='number.jpg'
image5 ='cake.jpg'
image6 = 'cookies.jpg'


attachments = []

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseived_message = event.text
        sender = event.user_id
        if reseived_message == "Привет":
            write_message(sender, "Добый день.ОСТОРОЖНО! Вызывает привыкание:", keyboard)
        elif reseived_message == "Пока":
            write_message(sender, "До свидания", keyboard)

        elif reseived_message == "Капкейки":
            write_message(sender, "Выбрать позицию:", keyboard1)
        elif reseived_message == "Классика":
            a = []
            attachments = a
            upload_image = upload.photo_messages(photos=image)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            send_photo(sender, "Крем-чиз (на основе натуральных сливок и творожного сыра), шоколадный ганаш(шоколад любой на ваш выбор)", keyboard1)
        elif reseived_message == "Капкейки + ягоды, фрукты":
            b = []
            attachments = b
            upload_image = upload.photo_messages(photos=image2)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            send_photo(sender, "Капкейки, украшенные шапкой крема с дополнительными сладостями - ягоды, фрукты (по сезону)", keyboard1)
        elif reseived_message == "Капкейки + пряники":
            c = []
            attachments = c
            upload_image = upload.photo_messages(photos=image3)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            send_photo(sender, "Капкейки, украшенные шапкой крема и имбирными пряниками", keyboard1)

        elif reseived_message == "Торты":
            write_message(sender, "Выбрать позицию:", keyboard2)
        elif reseived_message == "Торт сердце/цифра/буква/фигура":
            d = []
            attachments = d
            upload_image = upload.photo_messages(photos=image4)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            send_photo(sender, "Тонкие ароматные медовые коржи, прослоены легким  кремом", keyboard2)
        elif reseived_message == "Карамельный":
            e = []
            attachments = e
            upload_image = upload.photo_messages(photos=image5)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            send_photo(sender, "Нежный карамельный бисквит, соленая карамель,  под сливочным крем-чизом", keyboard2)

        elif reseived_message == "Пряники":
            write_message(sender, "Выбрать позицию:", keyboard3)
        elif reseived_message == "Пряники стандарт":
            f = []
            attachments = f
            upload_image = upload.photo_messages(photos=image6)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            send_photo(sender, "Прянички мы делаем из самых качественных и натуральных продуктов", keyboard3)
        elif reseived_message == "Пряничные букеты":
            g = []
            attachments = g
            upload_image = upload.photo_messages(photos=image7)[0]
            attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
            send_photo(sender, "Пряничные букеты (можно добавить меренги на палочке)", keyboard3)


        elif reseived_message == "Назад":
            write_message(sender, "Выбрать позицию:", keyboard)

        else:
            write_message(sender, "Доброго дня, на связи Алис&Co", keyboard)
