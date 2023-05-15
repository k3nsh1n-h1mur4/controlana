from django import forms
from django.forms import ModelForm, TextInput, DateInput, Select
from django.forms.widgets import Select

from .models import controlModel


class loginForm(forms.Form):
    username = forms.CharField(label='Usuario:', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Usuario:', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Usuario:', max_length=250, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class controlForm(forms.Form):

    ZONA = [
        ('ZONA METROPOLITANA', 'ZONA METROPOLITANA'),
        ('ZONA VALLARTA', 'ZONA VALLARTA'),
        ('ZONA TALA', 'ZONA TALA'),
        ('ZONA AUTLÁN', 'ZONA AUTLÁN'),
        ('ZONA LAGOS DE MORENO', 'ZONA LAGOS DE MORENO'),
        ('ZONA CD. GUMZÁN', 'ZONA CD. GUZMÁN'),
        ('ZONA OCOTLÁN', 'ZONA OCOTLÁN'),
    ]



    ppta = forms.CharField(label='# Propuesta', widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha =forms.CharField(label='Fecha', widget=forms.TextInput(attrs={'class':'form-control'}))
    aspirante = forms.CharField(label='Aspirante', widget=forms.TextInput(attrs={'class':'form-control'}))
    categoria = forms.CharField(label='Categroía', widget=forms.TextInput(attrs={'class':'form-control'}))
    propone = forms.CharField(label='Propone', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs={'class': 'form-control'}))
    zona = forms.ChoiceField(label='Zona', widget=forms.Select(attrs={'class': 'form-control'}), choices=ZONA)


class createUserForm(forms.Form):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Correo Electrónico', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class controlFormm(ModelForm):
    class Meta:
        ZONA = [
            ('ZONA METROPOLITANA', 'ZONA METROPOLITANA'),
            ('ZONA VALLARTA', 'ZONA VALLARTA'),
            ('ZONA TALA', 'ZONA TALA'),
            ('ZONA AUTLÁN', 'ZONA AUTLÁN'),
            ('ZONA LAGOS DE MORENO', 'ZONA LAGOS DE MORENO'),
            ('ZONA CD. GUMZÁN', 'ZONA CD. GUZMÁN'),
            ('ZONA OCOTLÁN', 'ZONA OCOTLÁN'),
        ]

        model = controlModel
        fields = '__all__'
        labels = {
            "ppta": "# de Propuesta",
            "fecha": "Fecha",
            "aspirante": "Aspirante",
            "categoria": "Categoría",
            "propone": "Propone",
            "telefono": "Teléfono",
            "zona": "Zona",
        }
        widgets = {
            "ppta": TextInput(attrs={'class': 'form-control'}),
            "fecha": TextInput(attrs={'class': 'form-control'}),
            "aspirante": TextInput(attrs={'class': 'form-control'}),
            "categoria": TextInput(attrs={'class': 'form-control'}),
            "propone": TextInput(attrs={'class': 'form-control'}),
            "telefono": TextInput(attrs={'class': 'form-control'}),
            "zona": Select(attrs={'class': 'form-control'}, choices=ZONA),
        }



#class createUserForm(forms.Form):
#    username = 
#    email = 
#    password =
