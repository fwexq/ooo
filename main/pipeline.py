import logging
import requests
from django.core.files.base import ContentFile


def get_avatar(backend, user, response, is_new=False, *args, **kwargs):
    if user is None:
        return

    if backend.name == 'vk-oauth2':
        avatar_url = response['photo_max']
    else:
        avatar_url = None

    if avatar_url and is_new:
        try:
            avatar_resp = requests.get(avatar_url, params={'type': 'large'})
            avatar_resp.raise_for_status()
        except requests.HTTPError as e:
            logging.error(e)
        else:
            avatar_file = ContentFile(avatar_resp.content)
            full_name = "%s %s" % (response['first_name'],
                                   response['last_name'])

            user.avatar.save("{0}.jpg".format(user.id), avatar_file)
            user.full_name = full_name
            user.save(update_fields=['avatar', 'full_name'])


# def get_avatar(backend, response, user=None, *args, **kwargs):
#     url = None
#
#     if backend.name == 'vk-oauth2':
#         url = response.get('photo', '')
#
#     if url:
#         user.profile.avatar = url
#         user.profile.save()
#         print(user.profile.avatar)