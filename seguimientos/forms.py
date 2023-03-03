from django import forms
from django.contrib.auth.models import User

opcionesEstados = [
    [0, "Habilitado"],
    [1, "Deshabilitado"]
]


class Registro(forms.Form):
    nombre = forms.CharField(required=True, min_length=5, max_length=40, label="Nombres", widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Nombre de Usuario'        
    }))
    apellido_paterno = forms.CharField(required=True, min_length=5, max_length=40, label="Apellido Paterno", widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Apellido Paterno de Usuario'        
    }))
    apellidoMaterno = forms.CharField(required=True, min_length=5, max_length=40,label="Apellido Materno", widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Apellido Materno de Usuario'        
    }))
    nombreUsuario = forms.CharField(required=True, min_length=5, max_length=40,label="Nombre Usuario", widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Usuario'        
    }))

    password = forms.CharField(label="Contraseña",required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Contraseña del Usuario'
    }))

    password2 = forms.CharField(label="Confirmar Contraseña",required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirmar contraseña del usuarios'
    }))
    correo = forms.EmailField(required=True, label="Correo",widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Correo del Usuario'
    }))
    celular = forms.IntegerField(required=True, label="Teléfono Celular", widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Celular del Usuario'
    }))
    tipoUsuario = forms.IntegerField(required=True, label="Tipo de Usuario", widget=forms.NumberInput(attrs={
        'class':'form-control'
    }))          
    estadoUsuario = forms.IntegerField(required=True, label="Estado Usuario", widget=forms.NumberInput(attrs={
        'class':'form-control'
        
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
            self.add_error('password2', 'Las contraseñas no son iguales')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
