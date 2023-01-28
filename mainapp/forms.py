from django import forms
from .models import EmotionText, DataText, DataName

emotions = [(x.id, x) for x in EmotionText.objects.all()]

class DataRow(forms.ModelForm):
    emotion_primary = forms.ChoiceField(
        choices=emotions,
        widget=forms.RadioSelect()
    )
    emotion_secondary = forms.ModelMultipleChoiceField(
        label='seconday emotions',
        queryset=EmotionText.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = DataText
        fields = '__all__'



    