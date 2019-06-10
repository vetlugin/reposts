import os
import vk_api
import requests
import telegram
from dotenv import load_dotenv
import argparse


def url_check(path):
    #return True if path[0:4]=='http://' else False
    return True if path.find('://') >= 0 else False


def vk_post(message, pic_path):
    try:
        vk_session = vk_api.VkApi(token=VK_TOKEN)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    upload = vk_api.VkUpload(vk_session)

    if not url_check(pic_path):
        photo = upload.photo(
            pic_path,
            album_id=263357401,
            group_id=VK_GROUP_ID
        )
        vk = vk_session.get_api()
        vk.wall.post(
            owner_id='{}'.format(photo[0]['owner_id']),
            from_group=1,
            message=message,
            attachments='photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
        )
    else:
        return


def telegram_post(message, pic_path):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id='@sphera_sveta', text=message)
    if url_check(pic_path):
        bot.send_photo(chat_id='@sphera_sveta', photo=pic_path)
    else:
        bot.send_photo(chat_id='@sphera_sveta', photo=open(pic_path, 'rb'))


def facebook_post(message, pic_path):

    context = f'https://graph.facebook.com/v3.3/{FACEBOOK_GROUP_ID}/photos'

    payload = {
        'caption':message,
        'access_token': FACEBOOK_TOKEN,
    }
    try:
        if not url_check(pic_path):
            open_file = open(pic_path, 'rb')
            files = {'file': open_file}
            response = requests.post(context, files=files, params=payload)
            if not response.ok:
                return
        else:
            payload['url'] = pic_path
            response = requests.post(context, params=payload)
        return response
    except KeyError:
        return


def main(message = 'Hello, World!', pic_path = 'empty.png'):

    vk_post(message, pic_path)
    telegram_post(message, pic_path)
    facebook_post(message, pic_path)

if __name__ == "__main__":

    load_dotenv()

    parser = argparse.ArgumentParser(description='Post message with picture to Vkontakte, Telegram and Facebook')
    parser.add_argument('message', help='Message to post')
    parser.add_argument('pic_path', help='Path to picture for posting')
    args = parser.parse_args()

    load_dotenv()

    VK_TOKEN=os.getenv("VK_TOKEN")
    VK_VERSION=os.getenv("VK_VERSION")
    VK_GROUP_ID=os.getenv("VK_GROUP_ID")
    TELEGRAM_TOKEN=os.getenv("TELEGRAM_TOKEN")
    FACEBOOK_GROUP_ID=os.getenv("FACEBOOK_GROUP_ID")
    FACEBOOK_TOKEN=os.getenv("FACEBOOK_TOKEN")

    message = args.message
    pic_path = args.pic_path

    main(message, pic_path)
