from django import forms
from .models import *


class PopEntryForm(forms.ModelForm):
    class Meta:
        model = Pop_Entry
        fields = (
            'character',
            'series',
            'series_number',
            'special_edition',
            'condition',
            'image',
        )

        widgets = {
            'character': forms.TextInput(attrs={'class': 'characters'}),
        }