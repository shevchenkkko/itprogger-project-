from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput,Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Назва новини'
            }),
            "anons":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Анонс новини'
            }),
            "date":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Дата публікації'
            }),
            "full_text":Textarea(attrs={
                'class':'form-control',
                'placeholder':'Текст новини'
            }) 
        }