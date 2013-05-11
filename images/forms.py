from django.forms import ModelForm
from models import Image

class ImageUploadForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'pathname']
