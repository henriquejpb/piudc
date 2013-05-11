class ImageRemote:
    def __init__(self, image):
        self.id = image.gphoto_id.text
        self.title = image.summary.text
        self.url = image.content.src

    def __unicode__(self):
        return "{id:" + self.id + ", title:" + self.title + ", url:" + self.url + "}"
