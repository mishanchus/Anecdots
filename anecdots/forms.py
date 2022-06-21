from django import forms
from .models import Anecdot

class AnecForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnecForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'
    class Meta:
        model = Anecdot
#        fields = '__all__'
        fields = ['text','category']
        widgets = {
            'text':    forms.Textarea(attrs={'class':"text", 'cols':70, 'rows': 15}),
            'category': forms.Select(attrs={'class': 'category'})
        }