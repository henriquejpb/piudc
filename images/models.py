from django.db import models
import PIL
import os.path
import uuid
from practica_PI import settings

UPLOAD_DIR = "pictures"
MAX_WIDTH = 600.0
MAX_HEIGHT = 600.0

class Image(models.Model):
    title = models.CharField(max_length=200)
    pathname = models.ImageField(upload_to=UPLOAD_DIR)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        fn, ext = os.path.splitext(self.pathname.name)
        new_filename = str(uuid.uuid4()) + ext
        self.pathname.name = new_filename

        super(Image, self).save(*args, **kwargs)

        filename = os.path.join(settings.BASE_DIR, self.pathname.url[1:])
        image = PIL.Image.open(filename)
    
        width, height = image.size
        if width > MAX_WIDTH or height > MAX_HEIGHT:
            factor = min(MAX_WIDTH/width, MAX_HEIGHT/height)
            print factor
            new_width = int(round(factor * width))
            new_height = int(round(factor * height))
        
            image.thumbnail((new_width, new_height), PIL.Image.ANTIALIAS)
            image.save(filename)

    def delete(self, *args, **kwargs):
        super(Image, self).delete(*args, **kwargs)
        self.pathname.storage.delete(self.pathname.path)
