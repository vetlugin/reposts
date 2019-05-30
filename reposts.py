import os
import vk_api
from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv("TOKEN")
GROUP_ID=os.getenv("GROUP_ID")
VK_VERSION=os.getenv("VK_VERSION")


def main():

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


if __name__ == '__main__':
    main()
