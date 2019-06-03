import os
import vk_api
import telegram
from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv("TOKEN")
TTOKEN=os.getenv("TTOKEN")
GROUP_ID=os.getenv("GROUP_ID")
VK_VERSION=os.getenv("VK_VERSION")


def vk_photo_post():
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


def main():
    bot = telegram.Bot(token=TTOKEN)
    print(bot.get_me())
    bot.send_message(chat_id='@sphera_sveta', text="I'm sorry Dave I'm afraid I can't do that.")
    bot.send_photo(chat_id='@sphera_sveta', photo='https://yadi.sk/i/_PE1oKs-kBmK0A')



if __name__ == '__main__':
    main()
