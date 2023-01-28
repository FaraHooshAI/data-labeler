from django import forms
from .models import EmotionText, DataText

class DataRow(forms.ModelForm):
    class Meta:
        model = EmotionText
        fields = ['data_name', 'text', 'emotion_primary', 'emotion_secondary']

    