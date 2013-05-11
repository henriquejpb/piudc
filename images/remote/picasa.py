import gdata.photos.service
import gdata.media
import gdata.geo
import urllib
import urlparse
from imageremote import ImageRemote
from images.models import Image, UPLOAD_DIR
from practica_PI import settings
import tempfile

import os

class RemoteModel:
    def __init__(self, 
            album_title="Album_Teste", album_description="Programacion Integrativa",
            client_login="programacion.integrativa@gmail.com", 
            client_password="PracticaProgramacionIntegrativa"):

        self.__photo_list = {}
        self.__content_type = "image/jpeg"

        self.__gd_client = gdata.photos.service.PhotosService()
        self.__gd_client.ClientLogin(client_login, client_password)

        self.__user_album = None
        albums = self.__gd_client.GetUserFeed()
        for album in albums.entry:
            if album.title.text == album_title:
                self.__user_album = album

        if self.__user_album == None:
            self.__user_album = self.__gd_client.InsertAlbum(title=album_title, summary=album_description)


    def get_list(self):
        photos = self.__gd_client.GetFeed("/data/feed/api/user/%s/albumid/%s?king=photo" %
                ("default", self.__user_album.gphoto_id.text))
        list = []
        for photo in photos.entry:
            self.__photo_list[photo.gphoto_id.text] = photo
            list.append(ImageRemote(photo))

        return list

    def download(self, id):
        if len(self.__photo_list) == 0:
            self.get_list()

        photo = ImageRemote(self.__photo_list[id])
        url = photo.url

        filename = os.path.basename(urlparse.urlsplit(url).path)
        filepath_relative = os.path.join(UPLOAD_DIR, filename)
        filepath = os.path.join(settings.MEDIA_ROOT, UPLOAD_DIR, filename)
        urllib.urlretrieve(photo.url, filepath)

        return photo, filepath_relative

    def upload(self, image):
        filename = os.path.basename(image.pathname.url)

        absolute_path = os.path.join(settings.BASE_DIR, image.pathname.url[1:])
        album_url = "/data/feed/api/user/%s/albumid/%s" % ("default", self.__user_album.gphoto_id.text)
        photo = self.__gd_client.InsertPhotoSimple(album_url, tempfile.mktemp(), 
                image.title, absolute_path, content_type=self.__content_type)
        return photo

    def delete(self, id):
        if len(self.__photo_list) == 0:
            self.get_list()

        photo = self.__photo_list[id]
        self.__gd_client.Delete(photo)



