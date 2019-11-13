from django import forms
import json

# Import Custom Models
from .models import Status


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 500:
            raise forms.ValidationError('Content is longer than 500 character')
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data

        content = data.get('content', None)
        image = data.get('image', None)

        if content == "":
            content = None

        if content is None and image is None:
            raise forms.ValidationError('Content or Image is required')
        return super().clean(*args, **kwargs)