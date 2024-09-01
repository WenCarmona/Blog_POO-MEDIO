from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categoria', 'autor']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if not titulo:
            raise forms.ValidationError('El titulo no puede estar vacio.')
        return titulo
    
    def clean_fecha_publicacion(self):
        fecha_publicacion = self.cleaned_data.get('fecha_publicacion')
        if fecha_publicacion > datetime.date.today():
            raise forms.ValidationError('La fecha de publicacion no puede ser fecha futura.')
        return fecha_publicacion