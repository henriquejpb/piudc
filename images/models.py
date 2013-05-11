from django.db import models
from PIL import Image

UPLOAD_DIR = "pictures"

class Image(models.Model):
    title = models.CharField(max_length=200)
    pathname = models.ImageField(upload_to=UPLOAD_DIR)

    def __unicode__(self):
        return self.title

    def delete(self, *args, **kwargs):
        super(Image, self).delete(*args, **kwargs)
        self.pathname.storage.delete(self.pathname.path)
