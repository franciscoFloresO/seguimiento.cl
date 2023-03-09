from django import forms
from django.contrib.auth.models import User

opcionesEstados = [
    [0, "Habilitado"],
    [1, "Deshabilitado"]
]

class Registro(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Nombre de Usuario'
        }))
    nombre = forms.CharField(required=True, min_length=5, max_length=40, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Nombre'
    })) 
    apellidoPaterno = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Apellido Paterno Usuario'        
    }))
    apellidoMaterno = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Apellido Materno Usuario'
        }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'class':'Contraseña'
    }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'class':'Contraseña'        
    }))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Correo'
    })) 
    telefono = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Teléfono'
        }))
    tipoUsuario = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Tipo de Usuario'
        }))
    estadoUsuario = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Estado de Usuario'
        }))
     
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Nombre de usuario ya está en uso')
        return username

    def clean_email(self):
        correo = self.cleaned_data.get('email')
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError('Correo ya está en uso')
        return correo

    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2','La contraseña no coinciden')


    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),            
            # self.cleaned_data.get('nombre'),
            # self.cleaned_data.get('apellidoPaterno'),
            # self.cleaned_data.get('apellidoMaterno'),            
            # self.cleaned_data.get('nombreUsuario'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
            # self.cleaned_data.get('celular'),
            # self.cleaned_data.get('tipoUsuario'),
            # self.cleaned_data.get('estadoUsuario')
        )
