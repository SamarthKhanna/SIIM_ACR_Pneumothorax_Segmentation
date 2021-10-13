from django import forms
from .models import Lungs


class LungForm(forms.ModelForm):
    class Meta:
        model = Lungs
        fields = ('input_image',)
        widgets = {
            'input_image': forms.FileInput(attrs={
                "accept": '.dcm'
            })
        }
        labels = {
            'input_image': 'Please upload the X-ray in DICOM format'
        }
