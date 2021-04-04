import requests


def create_folder(token_yandex, folder_name):
    token = token_yandex
    headers = {
        'Authorization': f'OAuth {token}'
    }

    response = requests.put(
        'https://cloud-api.yandex.net/v1/disk/resources',
        params={
            'path': str(folder_name)

        },
        headers=headers
    )

    return response.status_code





