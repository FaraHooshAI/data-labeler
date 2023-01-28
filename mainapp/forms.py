from django import forms
from .models import EmotionText, DataText, DataName

emotions = [(x.id, x) for x in EmotionText.objects.all()]
class DataRow(forms.ModelForm):
    class Meta:
        model = DataText
        fields = ['data_name', 'text']

    emotions_primary = forms.ChoiceField(
        choices= emotions,
        widget=forms.RadioSelect()
    )

    emotions_secondary = forms.ModelMultipleChoiceField(
        queryset= EmotionText.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )



    