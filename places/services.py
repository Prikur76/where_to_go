import os
import re
import urllib

import requests
from slugify import slugify


def get_short_title(title):
    """Возвращает короткое название экскурсии"""
    if '«' in title:
        pattern = r'«([А-ЯЁа-яёA-Za-z0-9\.\s\-\„\“]+)»'
        return re.search(pattern, title)[1]
    return title


def get_place_from_link(link):
    """Возвращает описание экскурсии из файла по ссылке"""
    response = requests.get(link)
    place = response.json()
    place['slug'] = slugify(place['title'])
    return place


def download_image_from_url(image_link, image_directory):
    """Скачивает картинку с интернета по ссылке через GET-запрос"""
    image_name = os.path.basename(urllib.parse.urlsplit(image_link).path)
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)
    response = requests.get(url=image_link)
    image_path = os.path.join(image_directory, image_name)
    if response.ok:
        with open(image_path, 'wb') as f:
            f.write(response.content)
    return image_name
