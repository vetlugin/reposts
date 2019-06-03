import os
import vk_api
import requests
import telegram
from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv("TOKEN")
TELEGRAM_TOKEN=os.getenv("TELEGRAM_TOKEN")
FACEBOOK_GROUP_ID=os.getenv("FACEBOOK_GROUP_ID")
FACEBOOK_TOKEN=os.getenv("FACEBOOK_TOKEN")
GROUP_ID=os.getenv("GROUP_ID")
VK_VERSION=os.getenv("VK_VERSION")


def vk_post():
    try:
        vk_session = vk_api.VkApi(token=TOKEN)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    upload = vk_api.VkUpload(vk_session)

    photo = upload.photo(
        'fotoshar.jpeg',
        album_id=263357401,
        group_id=182385389
    )

    vk = vk_session.get_api()

    vk.wall.post(
        owner_id='{}'.format(photo[0]['owner_id']),
        from_group=1,
        message='Привет - это шарик',
        attachments='photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
    )


def telegram_post():
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    print(bot.get_me())
    bot.send_message(chat_id='@sphera_sveta', text="I'm sorry Dave I'm afraid I can't do that.")
    bot.send_photo(chat_id='@sphera_sveta', photo='https://yadi.sk/i/_PE1oKs-kBmK0A')


def facebook_post():
    #context = f'https://graph.facebook.com/{FACEBOOK_GROUP_ID}/feed'

    context = f'https://graph.facebook.com/v3.3/{FACEBOOK_GROUP_ID}/photos'

    open_file = open('kino.jpg', 'rb')
    files = {'file': open_file}

    payload = {
        #'url': 'http://www.spherasveta.ru/img/image/hanty_13.jpg',
        'caption':'text and photo',
#        'message': "АЛЛЕЛУЙАА!",
        'access_token': FACEBOOK_TOKEN,
    }

    response = requests.post(context, files=files, params=payload)
    if not response.ok:
        return
    
    #response = requests.post(context, params=payload).json()
    try:
        print(response)
    except KeyError:
        return


def main():
    facebook_post()

if __name__ == '__main__':
    main()
