import os

import requests


def download_image_from_url(url, directory, name):
    """
    Скачивает картинку с интернета по ссылке через GET-запрос
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    response = requests.get(url)
    response.raise_for_status()
    img_path = os.path.join(directory, name)
    with open(img_path, 'wb') as f:
        f.write(response.content)
