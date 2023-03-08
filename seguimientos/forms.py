from django import forms
from django.contrib.auth.models import User

opcionesEstados = [
    [0, "Habilitado"],
    [1, "Deshabilitado"]
]

class NuevoUsuario(forms.Form):
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
    nombreUsuario = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Nombre de Usuario'
        }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'class':'Contraseña'
    }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'class':'Contraseña'        
    }))
    correo = forms.CharField(required=True, widget=forms.EmailInput(attrs={
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
     
    
    def clean_nombre(self):
        nombreUsuario = self.cleaned_data.get('nombreUsuario')
        if User.objects.filter(nombreUsuario=nombreUsuario).exists():
            raise forms.ValidationError('Nombre de usuario ya está en uso')
        return nombreUsuario

    def clean_email(self):
        correo = self.cleaned_data.get('correo')
        if User.objects.filter(correo=correo).exists():
            raise forms.ValidationError('Correo ya está en uso')
        return correo

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Las contraseñas no son iguales')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('nombre'),
            self.cleaned_data.get('apellidoPaterno'),
            self.cleaned_data.get('apellidoMaterno'),            
            self.cleaned_data.get('nombreUsuario'),
            self.cleaned_data.get('correo'),
            self.cleaned_data.get('password'),
            self.cleaned_data.get('celular'),
            self.cleaned_data.get('tipoUsuario'),
            self.cleaned_data.get('estadoUsuario')
        )
