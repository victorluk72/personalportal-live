from django import forms
from .models import Profile
from cloudinary.forms import CloudinaryFileField


class AvatarUploadForm(forms.ModelForm):
    avatar = CloudinaryFileField(
        options={
            'crop': 'thumb',
            'width': 90,
            'height': 160,
            'folder': 'avatars'
        }
    )

    class Meta:
        model = Profile
        fields = ('avatar', 'user')
